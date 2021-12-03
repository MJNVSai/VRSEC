# -*- coding: utf-8 -*-
"""
Created on Tue Sep 21 19:30:29 2021

free scale graph using barabasi_albert_graph() method

@author: Krishna
"""

import networkx as nx
import matplotlib.pyplot as plt

S = nx.barabasi_albert_graph(50,2)
# 50 is no.of nodes

nx.draw(S)
plt.show()

# saving the graph with a new file name as .gexf extension

nx.write_gexf(S,"network_graph.gexf")