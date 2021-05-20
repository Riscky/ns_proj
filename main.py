import networkx as nx
from sklearn.metrics.cluster import normalized_mutual_info_score
from networkx.algorithms import community
from cdlib import datasets
from cdlib import NodeClustering

# internal modules
import load
import algorithms

graphs = load.load_graphs()

for (graph, ground_truth) in graphs:
    for algorithm in algorithms.get():
        result = algorithm(graph, 0)
        print(result)
        score = ground_truth.normalized_mutual_information(result)
        print(score)
