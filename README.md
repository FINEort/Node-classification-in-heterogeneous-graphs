# Node-classification-in-heterogeneous-graphs
### 1.数据
#### 异质数据集：
| datasets | #Nodes | #Edges | #Features | #Classes | #Train/Val/Test |
| ------------- | ------------- | ------------- | ------------- | ------------- | ------------- |
| cornell | 183 | 298 | 1703 | 5 | 87/59/37 |
| texas | 183 | 325 | 1703 | 5 | 87/59/37 |
| wisconsin | 251 | 515 | 1703 | 5 | 120/80/51 |
| chameleon_filtered | 890 | 8854 | 2325 | 5 | 409/287/194 |
| squirrel_filtered | 2223 | 46998 | 2089 | 5 | 1053/718/452 |
| Actor | 7600 | 30019 | 932 | 5 | 3648/2432/1520 |
| roman_empire | 22662 | 32927 | 300 | 18 | 11331/5665/5666 |

#### 同质数据集：
| datasets | #Nodes | #Edges | #Features | #Classes | #Train/Val/Test |
| ------------- | ------------- | ------------- | ------------- | ------------- | ------------- |
| cora | 2708 | 10556 | 1433 | 7 | 140/500/1000 |
| citeseer | 3327 | 9104 | 3703 | 6 | 120/500/1000 |
| pubmed | 19717 | 88648 | 500 | 3 | 60/500/1000 |
### 2.模型
![image](https://github.com/user-attachments/assets/5461c15f-f0c7-4ab2-a289-817191a362a6)
### 3.实验
#### Figure 1. Accuracy of GAT and our model based on degrees gap
![texas](https://github.com/user-attachments/assets/c814ecf6-d552-4f06-8a6f-cadd6063ef75)
![wisconsin](https://github.com/user-attachments/assets/64fa631b-7a24-40b6-92ce-11b7d7214455)
#### Table 1. Node classification experiments in heterogeneous graphs
|          | cornell     | texas        | wisconsin    | chameleon    | squirrel     | Actor       | Roman Empire  |
|----------|-------------|--------------|--------------|--------------|--------------|-------------|---------------|
| GCN      | 41.08±5.6   | 58.92±5.9    | 53.92±4.1    | 34.75±1.6    | 28.66±1.8    | 28.59±1.1   | /             |
| GAT      | 48.11±5.1   | 59.46±5.8    | 59.22±5.9    | 38.72±3.2    | 33.89±1.3    | 28.38±1.5   | /             |
| GATv2    | 43.78±6.1   | 61.08±4.6    | 60.39±3.9    | 38.19±2.4    | 34.29±0.8    | 26.86±1.3   | /             |
| GPR-GNN  | 76.86 ± 7.1 | 81.51 ± 6.6  | 76.3±3.9     | 41.3±1.5     | 37.0±0.9     | 35.58 ± 0.9 | 78.5±0.4      |
| AERO-GNN | 81.24 ± 6.8 | 84.35 ± 5.2  | 84.80 ± 3.3  | 41.0±2.9     | 41.8±1.1     | 36.57 ± 1.1 | 76.8±0.3      |
| DGCN     | 77.9±3.1    | 75.8±3.5     | 76.9±1.4     | 42.3±2.3     | 40.6±1.0     | /           | 80.0±0.7      |
| DCM      | /           | 84.96 ± 5.60 | 85.36 ± 5.05 | 53.76 ± 3.72 | 35.13 ± 2.27 | /           | /             |
| ADPA     | 82.9±3.0    | 83.8±2.7     | 81.6±3.5     | 46.2±1.3     | 45.2±1.3     | /           | 84.3±0.3      |
| ours     | 77.84±3.3   | 85.41±5.0    | 85.69±3.2    | 40.95±7.0    | 33.13±1.6    | 36.90±2.8   |               |
#### Table 2. Node classification experiments in homogeneous graphs
|          | CoraML    | CiteSeer  | PubMed    |
|----------|-----------|-----------|-----------|
| GCN      | 84.2±0.5  | 65.3±0.5  | 79.2±0.4  |
| GAT      | 83.78±0.5 | 71.89±0.6 | 78.1900   |
| GATv2    | 83.88±0.6 | 71.15±1.2 | 78.2300   |
| GPR-GNN  | 84.7±0.7  | 64.7±0.7  | 79.3±0.4  |
| AERO-GNN | 83.9±0.8  | 63.0±0.6  | 79.5±0.6  |
| DGCN     | 83.1±1.0  | 63.2±0.8  | 77.9±0.4  |
| ADPA     | 84.5±0.6  | 66.0±0.4  | 80.2±0.4  |
| ours     | 81.67±0.9 | 70.84±0.3 |           |
#### Table 3. Ablation study
| attention | edgeMLP | simrank | cornell            | texas             | wisconsin          | chameleon          | squirrel    | Actor              |
|-----------|---------|---------|--------------------|-------------------|--------------------|--------------------|-------------|--------------------|
| w         | w       | w       | 0.778378378        | 0.854054054       | 0.856862745        | 0.4094689          | 0.331292708 | 0.369013157        |
| w         | w       | w/o     | 0.748648649        | 0.835135135       | 0.847058824        | 0.3600259          | 0.331782292 | 0.363552632        |
| w         | w/o     | w       | 0.681081081        | 0.748648649       | 0.739215686        | 0.361496732        | 0.319738197 | 0.337368421        |
| w/o       | w       | w       | 0.72972973         | 0.818918919       | 0.839215686        | 0.366286956        | 0.321593165 | 0.364013158        |

### 4.参考文献
Sun H, Li X, Wu Z, et al. Breaking the Entanglement of Homophily and Heterophily in Semi-supervised Node Classification[J]. arXiv preprint arXiv:2312.04111, 2023. [[paper]](https://arxiv.org/abs/2312.04111)(ADPA)

Battiloro C, Spinelli I, Telyatnikov L, et al. From latent graph to latent topology inference: Differentiable cell complex module[J]. arXiv preprint arXiv:2305.16174, 2023. [[paper]](https://arxiv.org/abs/2305.16174) [[code]](https://github.com/spindro/differentiable_cell-complex_module)(DCM)

Pan E, Kang Z. Beyond homophily: Reconstructing structure for graph-agnostic clustering[C]//International Conference on Machine Learning. PMLR, 2023: 26868-26877. [[paper]](https://proceedings.mlr.press/v202/pan23b.html)[[code]](https://github.com/Panern/DGCN)(DGCN)

Lee S Y, Bu F, Yoo J, et al. Towards deep attention in graph neural networks: Problems and remedies[C]//International Conference on Machine Learning. PMLR, 2023: 18774-18795. [[paper]](https://proceedings.mlr.press/v202/lee23b.html) [[code]](https://github.com/syleeheal/AERO-GNN)(AERO-GNN)
