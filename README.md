# Node-classification-in-heterogeneous-graphs
### 1.数据
异质数据集：
| datasets | #Nodes | #Edges | #Features | #Classes | #Train/Val/Test |
| ------------- | ------------- | ------------- | ------------- | ------------- | ------------- |
| cornell | 183 | 298 | 1703 | 5 | 87/59/37 |
| texas | 183 | 325 | 1703 | 5 | 87/59/37 |
| wisconsin | 251 | 515 | 1703 | 5 | 120/80/51 |
| chameleon_filtered | 890 | 8854 | 2325 | 5 | 409/287/194 |
| squirrel_filtered | 2223 | 46998 | 2089 | 5 | 1053/718/452 |
| Actor | 7600 | 30019 | 932 | 5 | 3648/2432/1520 |
| roman_empire | 22662 | 32927 | 300 | 18 | 11331/5665/5666 |

同质数据集：
| datasets | #Nodes | #Edges | #Features | #Classes | #Train/Val/Test |
| ------------- | ------------- | ------------- | ------------- | ------------- | ------------- |
| cora | 2708 | 10556 | 1433 | 7 | 140/500/1000 |
| citeseer | 3327 | 9104 | 3703 | 6 | 120/500/1000 |
| pubmed | 19717 | 88648 | 500 | 3 | 60/500/1000 |
### 2.模型
![image](https://github.com/user-attachments/assets/5461c15f-f0c7-4ab2-a289-817191a362a6)
### 3.实验
#### Table1: Node classification experiments in heterogeneous graphs
|          | Cornell     | Texas        | Wisconsin    | Chameleon    | Squirrel     | Roman Empire | Actor        |
|----------|-------------|--------------|--------------|--------------|--------------|--------------|--------------|
| GCN      | 45.135135   | 58.378378    | 52.941176    | 35.155755    | 29.171272    | -            | 28.907895    |
| GAT      | 44.05405405 | 58.91891892  | 57.84313725  | 38.41758381  | 33.84605722  | -            | 27.51973684  |
| GATv2    | 46.75675676 | 60.54054054  | 59.21568627  | 38.82351347  | 34.36295218  | -            | 26.98684211  |
| GPR-GNN  | 76.86 ± 7.1 | 81.51 ± 6.6  | 76.3±3.9     | 41.3±1.5     | 37.0±0.9     | 78.5±0.4     | 35.58 ± 0.9  |
| AERO-GNN | 81.24 ± 6.8 | 84.35 ± 5.2  | 84.80 ± 3.3  | 41.0±2.9     | 41.8±1.1     | 76.8±0.3     | 36.57 ± 1.1  |
| DGCN     | 77.9±3.1    | 75.8±3.5     | 76.9±1.4     | 42.3±2.3     | 40.6±1.0     | 80.0±0.7     | -            |
| DCM      | -           | 84.96 ± 5.60 | 85.36 ± 5.05 | 53.76 ± 3.72 | 35.13 ± 2.27 | -            | -            |
| ADPA     | 82.9±3.0    | 83.8±2.7     | 81.6±3.5     | 46.2±1.3     | 45.2±1.3     | 84.3±0.3     | -            |
| Ours     | 77.83783784 | 85.67567568  | 86.470588    | 40.94689355  | 33.12927076  | -            | 36.90131579  |
#### Table2: Node classification experiments in homogeneous graphs
|          | CoraML   | CiteSeer | PubMed    |
|----------|----------|----------|-----------|
| GCN      | 84.2±0.5 | 65.3±0.5 | 79.2±0.4  |
| GAT      | -        | 70.5300  | 78.1900   |
| GATv2    | -        | 71.4600  | 78.2300   |
| GPR-GNN  | 84.7±0.7 | 64.7±0.7 | 79.3±0.4  |
| AERO-GNN | 83.9±0.8 | 63.0±0.6 | 79.5±0.6  |
| DGCN     | 83.1±1.0 | 63.2±0.8 | 77.9±0.4  |
| ADPA     | 84.5±0.6 | 66.0±0.4 | 80.2±0.4  |
| ours     | -        | 70.8400  | -         |
### 4.参考文献
Sun H, Li X, Wu Z, et al. Breaking the Entanglement of Homophily and Heterophily in Semi-supervised Node Classification[J]. arXiv preprint arXiv:2312.04111, 2023. [[paper]](https://arxiv.org/abs/2312.04111)

Battiloro C, Spinelli I, Telyatnikov L, et al. From latent graph to latent topology inference: Differentiable cell complex module[J]. arXiv preprint arXiv:2305.16174, 2023. [[paper]](https://arxiv.org/abs/2305.16174) [[code]](https://github.com/spindro/differentiable_cell-complex_module)

Pan E, Kang Z. Beyond homophily: Reconstructing structure for graph-agnostic clustering[C]//International Conference on Machine Learning. PMLR, 2023: 26868-26877. [[paper]](https://proceedings.mlr.press/v202/pan23b.html)

Lee S Y, Bu F, Yoo J, et al. Towards deep attention in graph neural networks: Problems and remedies[C]//International Conference on Machine Learning. PMLR, 2023: 18774-18795. [[paper]](https://proceedings.mlr.press/v202/lee23b.html) [[code]](https://github.com/syleeheal/AERO-GNN)
