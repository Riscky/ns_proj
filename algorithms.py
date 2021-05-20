from networkx.algorithms import community
from cdlib import algorithms
from cdlib import NodeClustering

def kernighan_lin(G, seed):
    # TODO: bisect more then once
    KL = community.kernighan_lin_bisection(G, seed = seed)
    print(KL)
    return NodeClustering(KL, G)


def label_propagation(G, seed):
    # TODO: pass seed
    LP = community.asyn_lpa_communities(G)
    LP_list = list(LP)
    return NodeClustering(LP_list, G)

# TODO fix infomap
def info_map(G, seed):
    # TODO: pass seed
    return algorithms.infomap(G)

def louvain(G, seed):
    # TODO: pass seed
    return algorithms.louvain(G)

def get():
    return [kernighan_lin, label_propagation, louvain]
