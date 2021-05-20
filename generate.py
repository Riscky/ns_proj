import networkx as nx
import json

for size in [100, 500]:
    mu = 0.5

    G = nx.LFR_benchmark_graph(size, 2.5, 1.1, mu=mu, average_degree=5, max_community=50, seed=25, max_iters=5000)

    name = f'LFR_N{size}_ad5_mc50_mu{mu}'

    # save G to disk
    nx.write_adjlist(G, f'graphs/{name}')

    # save communities to disk
    firsts = filter(lambda x: min(G.nodes[x]["community"]) == x, G.nodes)
    groups = list(map(lambda x: list(G.nodes[x]["community"]), firsts))

    with open(f'communities/{name}', 'w') as file:
        json.dump(groups, file)
