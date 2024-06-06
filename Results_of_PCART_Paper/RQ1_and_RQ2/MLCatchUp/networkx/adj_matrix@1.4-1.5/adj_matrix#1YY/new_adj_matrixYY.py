import networkx as nx
G = nx.Graph()
G.add_edges_from([(1, 2), (1, 3), (2, 4), (2, 5), (3, 5)])
nodelist = [1, 2, 3, 4, 5]
adj_matrix = nx.adj_matrix(G, weight='weight')
