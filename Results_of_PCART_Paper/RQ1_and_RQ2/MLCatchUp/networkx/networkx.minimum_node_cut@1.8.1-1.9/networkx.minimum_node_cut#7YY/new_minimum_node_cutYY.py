import networkx as nx
G = nx.Graph()
G.add_edges_from([(1, 2), (1, 3), (2, 3), (2, 4), (3, 4)])
min_node_cut = nx.minimum_node_cut(G, None, t=None, flow_func=None)
