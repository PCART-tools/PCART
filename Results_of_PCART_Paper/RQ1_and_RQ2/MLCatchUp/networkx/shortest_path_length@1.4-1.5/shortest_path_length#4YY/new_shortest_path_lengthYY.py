import networkx as nx
G = nx.Graph()
G.add_edges_from([(1, 2), (1, 3), (2, 4), (3, 5), (4, 5)])
length = nx.shortest_path_length(G, source=1)
