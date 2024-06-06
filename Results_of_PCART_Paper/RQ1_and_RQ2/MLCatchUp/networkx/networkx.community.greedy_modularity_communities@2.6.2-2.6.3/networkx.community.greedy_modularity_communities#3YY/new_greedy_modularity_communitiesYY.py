import networkx as nx
G = nx.karate_club_graph()
communities = nx.community.greedy_modularity_communities(G, None, n_communities=1)
