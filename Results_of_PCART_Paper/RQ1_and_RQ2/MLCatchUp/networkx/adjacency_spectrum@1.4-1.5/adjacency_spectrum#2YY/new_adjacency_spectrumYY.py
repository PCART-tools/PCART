import networkx as nx
import numpy as np
G = nx.Graph()
G.add_edges_from([(1, 2), (1, 3), (2, 4), (2, 5), (3, 5)])
spectrum = nx.adjacency_spectrum(G=G, weight='weight')
