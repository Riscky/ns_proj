import networkx as nx
import json
import math

for size in [100, 500, 1000, 5000, 10000, 50000, 100000, 500000, 1000000, 5000000, 10000000]:
    print(size)
    mu = 0.5

    for i in range(0,30):
        try:
            G = nx.LFR_benchmark_graph(size, 2.5, 1.1, mu=mu, average_degree=20, max_degree=50, max_iters=5000)
        except:
            continue

        components = nx.connected_components(G)
        GC = G.subgraph(max(components, key=len))
        removed = list(filter(lambda x: not x in GC.nodes, range(0, size)))

        for node in GC.nodes:
            for r in removed:
                GC.nodes[node]["community"].discard(r)

        name = f'LFR_N{size}_ad5_mc50_mu{mu}_i{i}'

        # save G to disk
        nx.write_gpickle(GC, f'graphs/{name}')
