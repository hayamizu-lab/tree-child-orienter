import sys
import numpy as np
import matplotlib.pyplot as plt
import networkx as nx
import itertools
from itertools import combinations
import csv
import random

def generate_random_graph(n, r, filename):
    G = nx.Graph()
    nodes = list(range(0, n))

    while len(nodes) > 1:
        v = 2 if random.random() < r else 1

        if v == 1:
            selected_nodes = random.sample(nodes, 2)
            new_node = max(nodes) + 1
            G.add_node(new_node)
            G.add_edge(selected_nodes[0], new_node)
            G.add_edge(selected_nodes[1], new_node)
            nodes.remove(selected_nodes[0])
            nodes.remove(selected_nodes[1])
            nodes.append(new_node)
        else:
            selected_node = random.choice(nodes)
            new_nodes = [max(nodes) + 1, max(nodes) + 2]
            G.add_node(new_nodes[0])
            G.add_node(new_nodes[1])
            G.add_edge(selected_node, new_nodes[0])
            G.add_edge(selected_node, new_nodes[1])
            nodes.remove(selected_node)
            nodes.extend(new_nodes)

    # Processing for vertices of degree 4
    degree_four_vertices = [v for v in G.nodes() if G.degree(v) == 4]
    
    for i in degree_four_vertices:
        new_node = max(G.nodes) + 1
        G.add_node(new_node)
        adjacent_nodes = list(G.neighbors(i))
        sorted_adjacent_nodes = sorted(adjacent_nodes, reverse=True)
        for j in range(2):
            G.remove_edge(i, sorted_adjacent_nodes[j])
            G.add_edge(new_node, sorted_adjacent_nodes[j])
            G.add_edge(new_node, i)

    # Add pendant vertex and edge, as the number of leaves is reduced if reticulation is chosen first.
    for i in range(n):
        if G.degree(i) == 2:
            temp = max(G.nodes) + 1
            while temp in G.nodes:
                temp += 1
            G.add_node(temp)
            G.add_edge(i, temp)

    # Processing for vertices of degree 2 is performed until there are no more vertices of degree 2.
    while any(G.degree(i) == 2 for i in G.nodes()):
        # Processing for vertices of degree 2
        degree_two_vertices = [v for v in G.nodes() if G.degree(v) == 2]
        for i in degree_two_vertices:
            adjacent_nodes = list(G.neighbors(i))
            G.remove_edge(i, adjacent_nodes[0])
            G.remove_edge(i, adjacent_nodes[1])
            G.add_edge(adjacent_nodes[0], adjacent_nodes[1])

        # Delete vertices of degree 0
        degree_zero_vertices = [v for v in G.nodes() if G.degree(v) == 0]
        
        for i in degree_zero_vertices:
            G.remove_node(i)

    # If the number of vertices changes, the vertex labels are reassigned from 0.
    new_labels = {old_label: new_label for new_label, old_label in enumerate(G.nodes())}
    G = nx.relabel_nodes(G, new_labels)

    return G


# Input
input_str = input("Filename n r k: ")
inputs = input_str.split()
filename = inputs[0]
n = int(inputs[1])
r = float(inputs[2])
k = int(inputs[3])

for i in range(k):
  G = generate_random_graph(n, r, filename)
  # Drawing graphs(made binary)
  nx.draw(G, pos=nx.kamada_kawai_layout(G), with_labels=True, node_size=100, font_size=8, arrows=False, node_color='lightblue')
  plt.savefig(filename + '_' + str(i+1) +'.pdf', format='pdf')
  plt.close()
  adjacency_matrix = nx.adjacency_matrix(G).todense().astype(int)
  np.savetxt(filename + '_' + str(i+1) + '.csv', adjacency_matrix, delimiter=",", fmt="%d")
