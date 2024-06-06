import networkx as nx
G = nx.gnp_random_graph(5, 0.5)
centrality = nx.harmonic_centrality(G, None, distance=None, sources=None)
