# -*- coding: utf-8 -*-
"""
Created on Thu Sep 23 19:34:43 2021

SIX DEGREE SEPERATION - MEET YOUR FAVAROUTIES

@author: Krishna
"""

import networkx as nx
import numpy as np

G = nx.read_edgelist("facebook_combined.txt/facebook_combined.txt")
N = list(G.nodes())

print("length of list 'N': ",len(N))

spll = [] # spll = shortest path length list

for u in N:
    for v in N:
        if u!=v:
            l = nx.shortest_path(G,u,v)
            #print("shortest path between {} and {} is of length:  {}\n".format(u,v,l))
            spll.append(l)

# spl = shortest path length

min_spl = min(spll)
max_spl = max(spll)
avg_spl = np.average(spll)

print()

print("minimum shortest path length: ",min_spl)
print("maximum shortest path length: ",max_spl)
print("average shortest path length: ",avg_spl)