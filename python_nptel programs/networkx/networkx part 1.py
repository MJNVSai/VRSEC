# -*- coding: utf-8 -*-
"""
Created on Mon Sep 20 15:15:49 2021

INTRODUCTION TO NETWORKX MODULE

@author: Krishna
"""

import networkx as nx
import matplotlib.pyplot as plt

# normal method
g = nx.Graph()
g.add_node(1)
g.add_node(2)
g.add_node(3)

g.add_edge(1,2)
g.add_edge(2,3)
g.add_edge(3,1)

print("\n edges are: ",g.edges(),"\n nodes are: ",g.nodes())

nx.draw(g)
plt.show()

# another method
d = nx.complete_graph(10)

#here 10 is the no.of nodes

nx.draw(d)
plt.show()