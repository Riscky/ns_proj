import networkx as nx
from sklearn.metrics.cluster import normalized_mutual_info_score
from networkx.algorithms import community

G = nx.LFR_benchmark_graph(250, 3, 1.5, 0.1, average_degree=5, min_community=20, seed=10)

# simplify labeling
labeling = list(map(lambda x: min(G.nodes[x]["community"]), G.nodes))

def kernighan_lin(G, seed):
    KL = community.kernighan_lin_bisection(G, seed = seed)
    return list(map(lambda x: 0 if x in KL[0] else 1, G.nodes))

KL_labeling = kernighan_lin(G, 10)

# Normalized Mutual Information
score = normalized_mutual_info_score(labeling, KL_labeling)

print(score)
