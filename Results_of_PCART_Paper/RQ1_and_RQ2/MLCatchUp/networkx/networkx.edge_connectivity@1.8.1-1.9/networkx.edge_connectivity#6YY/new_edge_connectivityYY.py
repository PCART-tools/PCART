import networkx as nx
G = nx.Graph()
G.add_edges_from([(1, 2), (1, 3), (2, 3), (2, 4), (3, 4)])
connectivity = nx.edge_connectivity(G, None, None, flow_func=None)
print(connectivity)
