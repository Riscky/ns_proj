import networkx as nx
import os
from cdlib import NodeClustering
import json

def load_graphs():
    items = os.listdir('graphs')

    graphs = []

    for name in items:
        G = nx.read_adjlist(f'graphs/{name}')

        with open(f'communities/{name}', 'r') as file:
            data = file.read()

        clustering = json.loads(data)

        ground_truth = NodeClustering(clustering, G)

        graphs.append((G, ground_truth))

    return graphs