import networkx as nx
G = nx.Graph()
G.add_edges_from([(1, 2), (1, 3), (2, 3), (2, 4), (3, 4)])
connectivity = nx.node_connectivity(G, None, t=None, flow_func=None)
