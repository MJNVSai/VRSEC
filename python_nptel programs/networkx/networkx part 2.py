# -*- coding: utf-8 -*-
"""
Created on Mon Sep 20 15:45:04 2021

@author: Krishna
"""

import networkx as nx
import matplotlib.pyplot as plt

# another method
d = nx.complete_graph(15)

#here 15 is the no.of nodes

nx.draw(d)
plt.show()

# by using probablity method

a = nx.gnp_random_graph(10,2.5)

# here 10 is no.of nodes and 2.5 is the probablity between the edges or nodes

nx.draw(a)
plt.show()