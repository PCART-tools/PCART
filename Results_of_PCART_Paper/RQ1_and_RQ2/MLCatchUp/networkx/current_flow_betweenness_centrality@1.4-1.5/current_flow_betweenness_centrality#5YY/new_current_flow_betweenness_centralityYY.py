import networkx as nx
G = nx.Graph()
G.add_edges_from([(1, 2), (2, 3), (3, 4), (1, 3)])
cfbc = nx.current_flow_betweenness_centrality(G=G, normalized=True, weight='weight')
