import networkx as nx
G = nx.Graph()
G.add_edges_from([(1, 2), (1, 3), (2, 4), (3, 4)])
avg_length = nx.average_shortest_path_length(G=G)
