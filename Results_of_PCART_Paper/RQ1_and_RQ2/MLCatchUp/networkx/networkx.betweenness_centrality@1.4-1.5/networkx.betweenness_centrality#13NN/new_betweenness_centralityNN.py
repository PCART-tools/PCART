import networkx as nx
G = nx.gnp_random_graph(5, 0.5)
betweenness = nx.betweenness_centrality(G, normalized=True, endpoints=False, weight=False)
