import networkx as nx
G = nx.Graph()
G.add_edges_from([(1, 2), (2, 3), (3, 4), (4, 1), (1, 3)])
avg_neighbor_degree = nx.average_neighbor_degree(G, nodes=None, source=False, target='out', weight=None)
