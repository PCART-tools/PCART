import networkx as nx
G = nx.Graph()
G.add_edges_from([(1, 2), (1, 3), (2, 3), (3, 4), (4, 5), (5, 1)])
avg_clust = nx.average_clustering(G, nodes=False, weight=None, count_zeros=True)
