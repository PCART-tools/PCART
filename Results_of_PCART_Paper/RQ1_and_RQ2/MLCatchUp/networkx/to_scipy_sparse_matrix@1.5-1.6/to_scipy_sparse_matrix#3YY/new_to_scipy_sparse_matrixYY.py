import networkx as nx
G = nx.Graph()
G.add_edges_from([(1, 2), (1, 3), (2, 4), (3, 4)])
sparse_matrix = nx.to_scipy_sparse_matrix(G, None, weight='weight', format='csr')
