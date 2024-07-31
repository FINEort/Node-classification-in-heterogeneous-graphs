# Node-classification-in-heterogeneous-graphs
### 1.数据
#### 异质数据集：
| datasets | #Nodes | #Edges | #Features | #Classes | #Train/Val/Test | #heterophily |
| ------------- | ------------- | ------------- | ------------- | ------------- | ------------- | ------------- |
| cornell | 183 | 298 | 1703 | 5 | 87/59/37 | 0.89 |
| texas | 183 | 325 | 1703 | 5 | 87/59/37 | 0.90 |
| wisconsin | 251 | 515 | 1703 | 5 | 120/80/51 | 0.87 |
| chameleon_filtered | 890 | 8854 | 2325 | 5 | 409/287/194 | 0.80 |
| squirrel_filtered | 2223 | 46998 | 2089 | 5 | 1053/718/452 | 0.84 |
| Actor | 7600 | 30019 | 932 | 5 | 3648/2432/1520 | 0.79 |
| roman_empire | 22662 | 32927 | 300 | 18 | 11331/5665/5666 | 0.96 |

#### 同质数据集：
| datasets | #Nodes | #Edges | #Features | #Classes | #Train/Val/Test | #heterophily |
| ------------- | ------------- | ------------- | ------------- | ------------- | ------------- | ------------- |
| cora | 2708 | 10556 | 1433 | 7 | 140/500/1000 | 0.17 |
| citeseer | 3327 | 9104 | 3703 | 6 | 120/500/1000 | 0.29 |
| pubmed | 19717 | 88648 | 500 | 3 | 60/500/1000 | 0.21 |
### 2.模型
![image](https://github.com/user-attachments/assets/5461c15f-f0c7-4ab2-a289-817191a362a6)
### 3.实验
#### Figure 1. Accuracy of GAT and our model based on degrees gap
![texas](https://github.com/user-attachments/assets/c814ecf6-d552-4f06-8a6f-cadd6063ef75)
![wisconsin](https://github.com/user-attachments/assets/64fa631b-7a24-40b6-92ce-11b7d7214455)
#### Table 1. Node classification experiments in heterogeneous graphs
|          | cornell    | texas      | wisconsin  | chameleon | squirrel  | Actor        |
|----------|------------|------------|------------|-----------|-----------|--------------|
| GCN      | 41.08±5.6  | 58.92±5.9  | 53.92±4.1  | 34.75±1.6 | 28.66±1.8 | 28.59±1.1    |
| GAT      | 48.11±5.1  | 59.46±5.8  | 59.22±5.9  | 38.72±3.2 | 33.89±1.3 | 28.38±1.5    |
| GATv2    | 43.78±6.1  | 61.08±4.6  | 60.39±3.9  | 38.19±2.4 | 34.29±0.8 | 26.86±1.3    |
| GPR-GNN  | 76.86±7.1  | ___81.51±6.6___  | 76.3±3.9   | 41.3±1.5  | 37.0±0.9  | 35.58 ± 0.9  |
| CPGNN    | 70.27±5.12 | 75.68±5.12 | 76.47±6.16 | /         | /         | 35.59±0.86   |
| H2GCN    | 75.95±7.3  | 75.68±6.7  | ___80.59±2.9___  | /         | /         | 36.23±0.9    |
| WRGAT    | 76.49±6.7  | 76.76±4.0  | 79.61±5.1  | /         | /         | 36.15±1.0    |
| AERO-GNN | **80.4±2.8**  | 80.4±2.7   |  78.6±3.6  | 41.0±2.9  | ___41.8±1.1___  | ___36.57±1.1___    |
| DGCN     | 68.32±±4.3 | 71.53±7.2  | 65.52±4.7  | ___42.3±2.3___  | 40.6±1.0  | 33.74±0.25   |
| DiGCN    | 77.8±4.9   | 79.5±3.2   | 77.2±2.2   | **43.4±1.8**  | **42.0±1.7**  | 32.82±0.68   |
| ours     | ___77.84±3.3___  | **85.41±5.0**  | **85.69±3.2**  | 40.95±7.0 | 33.24±1.7 | **36.90±2.8**    |

#### Table 2. Node classification experiments in homogeneous graphs
|          | Cora      | CiteSeer  | PubMed    |
|----------|---------------|---------------|---------------|
| GCN      | 80.71±0.2     | 71.05±0.1     | 79.1±0.2      |
| GAT      | 82.24±0.7     | 70.19±0.4     | 78.42±0.3     |
| GATv2    | 82.62±0.4     | 71.42±0.7     | 78.34±0.4     |
| ours     | **83.09±0.3** | **71.53±0.3** | **79.28±0.3** |
#### Table 3. Ablation study
| edgeMLP | simrank | cornell            | texas             | wisconsin          | chameleon          | squirrel           | Actor              |
|---------|---------|--------------------|-------------------|--------------------|--------------------|--------------------|--------------------|
| w       | w       | **77.84±3.3**      | **85.41±5.0**     | **85.69±3.2**      | **40.95±7.0**      | 33.24±1.7          | **36.90±2.8**      |
| w       | w/o     | 69.73±5.1          | 80.54±5.1         | 78.63±5.1          | 36.47±2.2          | 33.12±1.7          | 34.69±1.3          |
| w/o     | w       | 72.97±5.8          | 77.03±4.1         | 79.61±3.7          | 35.90±2.7          | **33.25±1.6**      | 34.39±1.2          |
| w/o     | w/o     | 71.35±5.3          | 77.84±5.1         | 79.22±3.8          | 36.03±2.4          | 33.08±1.6          | 34.51±1.0          |

### 4.参考文献
Sun H, Li X, Wu Z, et al. Breaking the Entanglement of Homophily and Heterophily in Semi-supervised Node Classification[J]. arXiv preprint arXiv:2312.04111, 2023. [[paper]](https://arxiv.org/abs/2312.04111)(ADPA)

Battiloro C, Spinelli I, Telyatnikov L, et al. From latent graph to latent topology inference: Differentiable cell complex module[J]. arXiv preprint arXiv:2305.16174, 2023. [[paper]](https://arxiv.org/abs/2305.16174) [[code]](https://github.com/spindro/differentiable_cell-complex_module)(DCM)

Pan E, Kang Z. Beyond homophily: Reconstructing structure for graph-agnostic clustering[C]//International Conference on Machine Learning. PMLR, 2023: 26868-26877. [[paper]](https://proceedings.mlr.press/v202/pan23b.html)[[code]](https://github.com/Panern/DGCN)(DGCN)

Lee S Y, Bu F, Yoo J, et al. Towards deep attention in graph neural networks: Problems and remedies[C]//International Conference on Machine Learning. PMLR, 2023: 18774-18795. [[paper]](https://proceedings.mlr.press/v202/lee23b.html) [[code]](https://github.com/syleeheal/AERO-GNN)(AERO-GNN)
