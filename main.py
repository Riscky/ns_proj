import networkx as nx
from sklearn.metrics.cluster import normalized_mutual_info_score
from networkx.algorithms import community
from cdlib import datasets
from cdlib import NodeClustering

#G = nx.LFR_benchmark_graph(500000, 2.5, 1.2, 0.1, average_degree=20, min_community=20, seed=10)

print(datasets.available_networks())

(G, ground) = datasets.fetch_network_ground_truth('LFR_N100000_ad5_mc50_mu0.3', 'networkx')

print('1')

# simplify labeling
#labeling = list(map(lambda x: min(G.nodes[x]["community"]), G.nodes))

print('2')

def kernighan_lin(G, seed):
    KL = community.kernighan_lin_bisection(G, seed = seed)
    return KL
    # print(KL)
    # return list(map(lambda x: 0 if x in KL[0] else 1, G.nodes))


def label_propagation(G, seed):
    LP = community.asyn_lpa_communities(G)
    LP_list = list(LP)
    return LP_list

    # labeling = []
    # for node in G.nodes:
    #     for c in LP_list:
    #         if node in c:
    #             labeling.append(min(c))

    # return labeling

# # https://github.com/mapequation/infomap/blob/master/examples/python/infomap-networkx.py


KL_labeling = NodeClustering(kernighan_lin(G, 10), G)
LP_labeling = NodeClustering(label_propagation(G, 0), G)

print('3')
#print(LP_labeling)

# Normalized Mutual Information
#score = normalized_mutual_info_score(labeling, LP_labeling)

score = ground.normalized_mutual_information(LP_labeling)

print('4')

print(score)
