import networkx as nx
G = nx.Graph()
G.add_edges_from([(1, 2), (1, 3), (2, 3), (3, 4), (4, 5), (5, 1)])
clust_coeff = nx.clustering(G,  None,  False)
