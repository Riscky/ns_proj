import networkx as nx
import os
from cdlib import NodeClustering
import json

def graphs():
    return os.listdir('graphs')

def load(name):
    G = nx.read_gpickle(f'graphs/{name}')

    # create NodeClustering object from community labels
    firsts = filter(lambda x: min(G.nodes[x]["community"]) == x, G.nodes)
    groups = list(map(lambda x: list(G.nodes[x]["community"]), firsts))
    ground_truth = NodeClustering(groups, G)

    return (G, ground_truth)
