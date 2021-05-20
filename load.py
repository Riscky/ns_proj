import networkx as nx
import os
from cdlib import NodeClustering
import json

def load_graphs():
    items = os.listdir('graphs')

    graphs = []

    for name in items:
        G = nx.read_gpickle(f'graphs/{name}')

        # create NodeClustering object from community labels
        firsts = filter(lambda x: min(G.nodes[x]["community"]) == x, G.nodes)
        groups = list(map(lambda x: list(G.nodes[x]["community"]), firsts))
        ground_truth = NodeClustering(groups, G)

        graphs.append((G, ground_truth))

    return graphs
