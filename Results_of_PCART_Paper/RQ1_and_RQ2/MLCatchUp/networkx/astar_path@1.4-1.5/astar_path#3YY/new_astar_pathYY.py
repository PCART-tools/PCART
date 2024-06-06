import networkx as nx
G = nx.Graph()
G.add_edges_from([(1, 2), (2, 3), (3, 4), (4, 5)])

def heuristic(u, v):
    return abs(u - v)
path = nx.astar_path(G, source=1, target=5, weight='weight')
