import networkx as nx
import pandas as pd
G = nx.gnp_random_graph(5, 0.5)
edgelist_df = nx.to_pandas_edgelist(G, source='source', edge_key=None)
