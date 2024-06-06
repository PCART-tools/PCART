import networkx as nx
G1 = nx.Graph()
G1.add_edges_from([(1, 2), (2, 3), (3, 1)])
G2 = nx.Graph()
G2.add_edges_from([(4, 5), (5, 6), (6, 4)])
isomorphic = nx.is_isomorphic(G1, G2=G2)
