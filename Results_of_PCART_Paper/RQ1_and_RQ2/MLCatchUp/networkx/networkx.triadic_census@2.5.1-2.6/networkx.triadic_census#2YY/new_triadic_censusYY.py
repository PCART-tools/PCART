import networkx as nx
G = nx.DiGraph()
G.add_edges_from([(1, 2), (2, 3), (3, 1)])
triadic_census_result = nx.triadic_census(G=G, nodelist=None)
