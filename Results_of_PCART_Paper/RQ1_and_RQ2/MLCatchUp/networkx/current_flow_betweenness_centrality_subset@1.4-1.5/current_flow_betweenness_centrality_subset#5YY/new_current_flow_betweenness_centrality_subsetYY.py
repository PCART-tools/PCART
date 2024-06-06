import networkx as nx

def generate_connected_graph(n, p, max_attempts=100):
    for _ in range(max_attempts):
        G = nx.gnp_random_graph(n, p)
        if nx.is_connected(G):
            return G
    raise Exception('Failed to generate a connected graph after several attempts')
G = generate_connected_graph(5, 0.5)
sources = [0, 1]
targets = [2, 3]
centrality = nx.current_flow_betweenness_centrality_subset(G, sources, targets, True, weight='weight')
