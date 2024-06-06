import networkx as nx
G = nx.gnp_random_graph(5, 0.5)
closeness = nx.closeness_centrality(G=G, v=None, normalized=True, distance=False)
