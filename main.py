import networkx as nx
from sklearn.metrics.cluster import normalized_mutual_info_score
from networkx.algorithms import community
from cdlib import datasets
from cdlib import NodeClustering
import time
import csv

# internal modules
import load
import algorithms

#graphs = [datasets.fetch_network_ground_truth(net_name='karate_club', net_type='networkx')]
graphs = load.load_graphs()

graph_info = []
results = []

with open('results.csv', 'a') as file:
    file.write('graph name, algorithm, score, time \n')

    for (graph_name, graph, ground_truth) in graphs:
        graph_info.append((graph_name, len(graph.nodes), len(graph.edges)))

        for name, algorithm in algorithms.get().items():
            before = time.process_time()
            result = algorithm(graph)
            after = time.process_time()
            score = ground_truth.normalized_mutual_information(result)

            file.write(f'{graph_name}, {name}, {score.score}, {after-before} \n')

print(graph_info)
