import networkx as nx
import json

for size in [100, 500]:
    mu = 0.5

    G = nx.LFR_benchmark_graph(size, 2.5, 1.1, mu=mu, average_degree=5, max_community=50, seed=25, max_iters=5000)
    # giant component
    # GC = G.subgraph(max(nx.connected_components(G), key=len))

    name = f'LFR_N{size}_ad5_mc50_mu{mu}'

    # save G to disk
    nx.write_gpickle(GC, f'graphs/{name}')
