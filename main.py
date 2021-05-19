import networkx as nx
from sklearn.metrics.cluster import normalized_mutual_info_score
from networkx.algorithms import community
from cdlib import datasets
from cdlib import NodeClustering
from algo import algo

#G = nx.LFR_benchmark_graph(500, 2, 1.1, 0.1, min_degree=20, max_degree=50, seed=10, max_iters=5000)


# save G to disk

#nx.write_adjlist(G, 'test')


print(datasets.available_networks())

exit()

(G, ground) = datasets.fetch_network_ground_truth('LFR_N1000_ad5_mc50_mu0.5', 'networkx')

Alabel = algo(G)
Alabeling = NodeClustering(Alabel, G)

# simplify labeling
#labeling = list(map(lambda x: min(G.nodes[x]["community"]), G.nodes))


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


#KL_labeling = NodeClustering(kernighan_lin(G, 10), G)
#LP_labeling = NodeClustering(label_propagation(G, 0), G)

#print(LP_labeling)

# Normalized Mutual Information
#score = normalized_mutual_info_score(labeling, LP_labeling)

score = ground.normalized_mutual_information(Alabeling)


print(score)
