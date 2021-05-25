from networkx.algorithms import community
from cdlib import algorithms
from cdlib import NodeClustering

def label_propagation(G, seed):
    LP = community.asyn_lpa_communities(G)
    LP_list = list(LP)
    return NodeClustering(LP_list, G)

def info_map(G, seed):
    return algorithms.infomap(G)

def louvain(G, seed):
    return algorithms.louvain(G)

def fluid(G, seed):
    return algorithms.async_fluid(G, 20)

def get():
    return {
        "label propagation": label_propagation,
        "infomap": info_map,
        "louvain": louvain,
        "fluid": fluid
    }
