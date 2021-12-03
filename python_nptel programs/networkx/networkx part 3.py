# -*- coding: utf-8 -*-
"""
Created on Tue Sep 21 19:22:38 2021

INTRODUCTION TO NETWORKX MODULE PATR - 2

@author: Krishna
"""

import networkx as nx
import matplotlib.pyplot as plt

G = nx.gnp_random_graph(50,0.3)

# here 50 is no.of nodes and 0.3 is probablity of edges
'''
print("edges are : ",G.edges())
print()
print("nodes are: ",G.nodes())
'''
nx.draw(G)
plt.show() 