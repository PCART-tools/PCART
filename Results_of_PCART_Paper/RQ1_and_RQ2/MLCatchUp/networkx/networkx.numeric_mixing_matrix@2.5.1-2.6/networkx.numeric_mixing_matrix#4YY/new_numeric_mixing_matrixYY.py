import networkx as nx
G = nx.Graph()
G.add_node(1, age=25)
G.add_node(2, age=30)
G.add_node(3, age=22)
G.add_node(4, age=35)
G.add_edges_from([(1, 2), (2, 3), (3, 4), (4, 1)])
M = nx.numeric_mixing_matrix(G, 'age', None, mapping=None)
