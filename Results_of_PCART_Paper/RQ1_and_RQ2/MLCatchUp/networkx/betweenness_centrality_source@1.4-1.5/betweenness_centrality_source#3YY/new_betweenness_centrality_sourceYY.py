import networkx as nx
import random
G = nx.gnp_random_graph(5, 0.5)
nx.betweenness_centrality_source(G,  True)
