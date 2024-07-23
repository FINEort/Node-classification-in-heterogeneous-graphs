import numpy as np
import scipy.sparse as sp
import torch, os
import torch_geometric.datasets as geo_data
from torch_geometric.data import Data, InMemoryDataset
import torch_geometric.transforms as T


DATA_ROOT = 'data'
if not os.path.isdir(DATA_ROOT):
    os.mkdir(DATA_ROOT)


class other_datasets(InMemoryDataset):
    def __init__(self, root, transform=None, pre_transform=None):
        super().__init__(root, transform, pre_transform)
        self.data, self.slices = torch.load(self.processed_paths[0])
    @property
    def raw_file_names(self):
        return ['some_file_1', 'some_file_2', ...]
    @property
    def processed_file_names(self):
        return ['data.pt']

    def process(self):
        # Read data into huge `Data` list.
        name = self.root.split("\\", 1)[1]
        data = other_data(name)
        data_list = [data]

        if self.pre_filter is not None:
            data_list = [data for data in data_list if self.pre_filter(data)]

        if self.pre_transform is not None:
            data_list = [self.pre_transform(data) for data in data_list]

        data, slices = self.collate(data_list)
        torch.save((data, slices), self.processed_paths[0])


def other_data(name):
    data_npz = np.load(os.path.join('data', f'{name.replace("-", "_")}.npz'))

    x = torch.tensor(data_npz['node_features'])
    y = torch.tensor(data_npz['node_labels'])
    edge_index = torch.tensor(data_npz['edges']).T
    train_mask = torch.tensor(data_npz['train_masks']).T
    val_mask = torch.tensor(data_npz['val_masks']).T
    test_mask = torch.tensor(data_npz['test_masks']).T

    data = Data(x=x, edge_index=edge_index, y=y, train_mask=train_mask, val_mask=val_mask, test_mask=test_mask)
    return data


def load_data(data_names='cora', normalize_feature=True, keep_unnormalize_A=True, sparse_adj=True):
    data_names = data_names.split()
    datas = {}
    for data_name in data_names:
        if data_name in ['cora', 'citeseer', 'pubmed']:
            data = geo_data.Planetoid(os.path.join(DATA_ROOT, data_name), data_name).data
            data.train_mask = data.train_mask.unsqueeze(1).expand(-1, 10).contiguous()
            data.val_mask = data.val_mask.unsqueeze(1).expand(-1, 10).contiguous()
            data.test_mask = data.test_mask.unsqueeze(1).expand(-1, 10).contiguous()
            datas[data_name] = data
        elif data_name in ['cora_ml']:
            data = geo_data.CitationFull(os.path.join(DATA_ROOT, data_name), data_name).data
            train_mask = torch.zeros(data.num_nodes, dtype=torch.bool)
            val_mask = torch.zeros(data.num_nodes, dtype=torch.bool)
            test_mask = torch.zeros(data.num_nodes, dtype=torch.bool)
            train_mask[:140] = True
            val_mask[200:700] = True
            test_mask[700:1700] = True
            data.train_mask = train_mask
            data.val_mask = val_mask
            data.test_mask = test_mask
            data.train_mask = data.train_mask.unsqueeze(1).expand(-1, 10).contiguous()
            data.val_mask = data.val_mask.unsqueeze(1).expand(-1, 10).contiguous()
            data.test_mask = data.test_mask.unsqueeze(1).expand(-1, 10).contiguous()
            datas[data_name] = data
        elif data_name in ['cornell', 'texas', 'wisconsin']:
            datas[data_name] = geo_data.WebKB(os.path.join(DATA_ROOT, data_name), data_name).data
        elif data_name in ['Actor']:
            datas[data_name] = geo_data.Actor(os.path.join(DATA_ROOT, data_name), T.NormalizeFeatures()).data
        elif data_name in ['chameleon', 'squirrel']:
            datas[data_name] = geo_data.WikipediaNetwork(os.path.join(DATA_ROOT, data_name), data_name).data
        elif data_name in ['chameleon_filtered', 'squirrel_filtered', 'roman_empire']:
            datas[data_name] = other_datasets(root="data/" + data_name).data
        else:
            datas[data_name] = geo_data.Coauthor(os.path.join(DATA_ROOT, data_name), data_name, T.NormalizeFeatures()).data

    for key in datas:
        data = datas[key]

        # # original split
        data.train_mask = data.train_mask.type(torch.bool)
        data.val_mask = data.val_mask.type(torch.bool)
        data.test_mask = data.test_mask.type(torch.bool)

        n = len(data.x)

        adj = sp.csr_matrix((np.ones(data.edge_index.shape[1]), data.edge_index), shape=(n, n))
        adj = adj + adj.T.multiply(adj.T > adj) - adj.multiply(adj.T > adj) + sp.eye(adj.shape[0])

        if keep_unnormalize_A:
            data.unnormalize_A = adj
        adj = normalize_adj(adj)  # symmetric normalization works bad, but why? Test more.
        data.A = adj
        if sparse_adj:
            data.adj = to_torch_sparse(adj)
        if normalize_feature:
            data.x = row_l1_normalize(data.x)

    return datas


def row_l1_normalize(X):
    norm = 1e-6 + X.sum(dim=1, keepdim=True)
    return X / norm


def to_torch_sparse(sparse_mx):
    """Convert a scipy sparse matrix to a torch sparse tensor."""
    sparse_mx = sparse_mx.tocoo().astype(np.float32)
    indices = torch.from_numpy(
        np.vstack((sparse_mx.row, sparse_mx.col)).astype(np.int64))
    values = torch.from_numpy(sparse_mx.data)
    shape = torch.Size(sparse_mx.shape)
    return torch.sparse.FloatTensor(indices, values, shape)


def normalize_adj(adj):
    """Symmetrically normalize adjacency matrix."""
    # add self-loop and normalization also affects performance a lot
    rowsum = np.array(adj.sum(1))
    d_inv_sqrt = np.power(rowsum, -0.5).flatten()
    d_inv_sqrt[np.isinf(d_inv_sqrt)] = 0.
    d_mat_inv_sqrt = sp.diags(d_inv_sqrt)
    return adj.dot(d_mat_inv_sqrt).transpose().dot(d_mat_inv_sqrt).tocoo()
