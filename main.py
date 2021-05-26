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

graph_info = []
results = []

with open('results.csv', 'a') as file:
    file.write('graph name, algorithm, score, time\n')

    for graph_name in load.graphs():
        (graph, ground_truth) = load.load(graph_name)
        info = (graph_name, len(graph.nodes), len(graph.edges))
        print(info)
        graph_info.append(info)

        for name, algorithm in algorithms.get().items():
            before = time.process_time()
            result = algorithm(graph)
            after = time.process_time()
            score = ground_truth.normalized_mutual_information(result)

            file.write(f'{graph_name}, {name}, {score.score}, {after-before}\n')

with open('graph.csv', 'a') as file:
    file.write('graph name, nodes, edges\n')
    for (name, nodes, edge) in graph_info:
        file.write(f'{name}, {nodes}, {edges}\n')
