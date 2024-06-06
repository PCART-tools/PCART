import networkx as nx
G = nx.Graph()
G.add_edges_from([(1, 2), (2, 3), (3, 4), (4, 5)])
vitality = nx.closeness_vitality(G=G, v=None)
print(vitality)
