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
    file.write('graph name, algorithm, score, time \n')

    for graph_name in load.graphs():
        (graph, ground_truth) = load.load(graph_name)
        graph_info.append((graph_name, len(graph.nodes), len(graph.edges)))

        for name, algorithm in algorithms.get().items():
            before = time.process_time()
            result = algorithm(graph)
            after = time.process_time()
            score = ground_truth.normalized_mutual_information(result)

            file.write(f'{graph_name}, {name}, {score.score}, {after-before} \n')

print(graph_info)
