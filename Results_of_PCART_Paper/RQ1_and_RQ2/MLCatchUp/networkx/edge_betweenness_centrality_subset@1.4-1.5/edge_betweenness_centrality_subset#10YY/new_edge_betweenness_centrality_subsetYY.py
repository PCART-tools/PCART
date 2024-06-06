import networkx as nx
import random
G = nx.gnp_random_graph(5, 0.5)
sources = random.sample(G.nodes(), 2)
targets = random.sample(G.nodes(), 2)
edge_betweenness = nx.edge_betweenness_centrality_subset(G,  sources,  targets,  False,  False)
