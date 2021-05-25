import networkx as nx
from sklearn.metrics.cluster import normalized_mutual_info_score
from networkx.algorithms import community
from cdlib import datasets
from cdlib import NodeClustering

# internal modules
import load
import algorithms

#graphs = [datasets.fetch_network_ground_truth(net_name='karate_club', net_type='networkx')]
graphs = load.load_graphs()

for (graph, ground_truth) in graphs:
    for name, algorithm in algorithms.get().items():
        result = algorithm(graph, 0)
        score = ground_truth.normalized_mutual_information(result)

        print(len(graph.nodes()))
        print(name)
        print(score)
