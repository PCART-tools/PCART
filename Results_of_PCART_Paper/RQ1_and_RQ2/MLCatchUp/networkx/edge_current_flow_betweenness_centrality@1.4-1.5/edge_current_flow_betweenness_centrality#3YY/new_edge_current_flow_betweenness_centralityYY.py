import networkx as nx

def generate_connected_graph(n, p, max_attempts=100):
    for _ in range(max_attempts):
        G = nx.gnp_random_graph(n, p)
        if nx.is_connected(G):
            return G
    raise Exception('Failed to generate a connected graph after several attempts')
G = generate_connected_graph(5, 0.5)
centrality = nx.edge_current_flow_betweenness_centrality(G, True, weight='weight')
