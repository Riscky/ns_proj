from networkx.algorithms import community
from cdlib import algorithms
from cdlib import NodeClustering

def label_propagation(G):
    LP = community.asyn_lpa_communities(G)
    LP_list = list(LP)
    return NodeClustering(LP_list, G)

def info_map(G):
    return algorithms.infomap(G)

def louvain(G):
    return algorithms.louvain(G)

def fluid(G):
    return algorithms.async_fluid(G, 25)

def get():
    return {
        "label propagation": label_propagation,
        "infomap": info_map,
        "louvain": louvain,
        "fluid": fluid
    }
