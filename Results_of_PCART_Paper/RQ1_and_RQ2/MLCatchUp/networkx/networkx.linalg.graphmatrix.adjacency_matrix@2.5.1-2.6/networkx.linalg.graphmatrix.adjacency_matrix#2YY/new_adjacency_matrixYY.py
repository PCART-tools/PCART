import networkx as nx
G = nx.Graph()
G.add_edges_from([(1, 2), (1, 3), (2, 4)])
adj_matrix = nx.adjacency_matrix(G=G, dtype=None)
