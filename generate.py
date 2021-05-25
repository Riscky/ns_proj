import networkx as nx
import json

for size in [100, 500]:
    mu = 0.5

    G = nx.LFR_benchmark_graph(size, 2.5, 1.1, mu=mu, average_degree=5, max_community=50, seed=25, max_iters=5000)

    components = nx.connected_components(G)
    GC = G.subgraph(max(components, key=len))
    removed = list(filter(lambda x: not x in GC.nodes, range(0, size)))

    for node in GC.nodes:
        for r in removed:
            GC.nodes[node]["community"].discard(r)

    name = f'LFR_N{size}_ad5_mc50_mu{mu}'

    # save G to disk
    nx.write_gpickle(GC, f'graphs/{name}')
