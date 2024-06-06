import networkx as nx
G = nx.karate_club_graph()
cliques = list(nx.find_cliques(G=G, nodes=None))
