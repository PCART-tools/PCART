import networkx as nx
G = nx.Graph()
G.add_edges_from([(1, 2), (2, 3), (3, 4), (4, 5)])

def heuristic(u, v):
    return abs(u - v)
path_length = nx.astar_path_length(G, 1, target=5, heuristic=heuristic, weight='weight')
