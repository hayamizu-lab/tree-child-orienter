import sys
import numpy as np
import matplotlib.pyplot as plt
import networkx as nx
import csv
import itertools
import time

def start():
    global start_time
    start_time = time.perf_counter()

def end(tag="Elapsed time"):
    if "start_time" in globals():
        print("{}: {:.9f} [sec]".format(tag, time.perf_counter() - start_time))
    else:
        print("Function start is not called.")

# Function readcsv
def readcsv(filename):
    distance_matrix = []
    data = []
    with open(filename + '.csv', 'r', encoding='utf-8') as file:
        csv_reader = csv.reader(file, delimiter=',')  # Specify the delimiter
        for row in csv_reader:
            row = [float(value) for value in row]
            distance_matrix.append(row)
    G = nx.from_numpy_array(np.array(distance_matrix))
    return G

# Checking whether tree-child
def is_tree_child(graph, indeg, i):
  if len(list(graph.successors(i))) == 0:
    return True
  for j in graph.successors(i):
    if indeg[j] == 1:
      return True
  return False

# Function select_vertices
def select_vertices(n, r):
  # Create a list of vertices
  vertices = list(range(n))
  # Generate vertex combinations using the combinations function
  selected_vertices = list(itertools.combinations(vertices, r))
  return selected_vertices

# Function orientation
def orientation(G, e_rho, v_num):
  N = nx.Graph()
  N.add_nodes_from(range(v_num))

  # Inserting a root
  root = max(N.nodes) + 1
  N.add_node(root)
  N.add_edge(root, e_rho[0])
  N.add_edge(root, e_rho[1])

  return N
  
def find_max_distance_set(G, r_set):
    max_distance = float('-inf')
    max_distance_sets = []

    for r in r_set:
        sum_distance = 0
        for u, v in itertools.combinations(r, 2):
            distance = nx.shortest_path_length(G, u, v)
            if distance <= 1:
                sum_distance += distance - 100
            else:
                sum_distance += distance

        if sum_distance > max_distance:
            max_distance = sum_distance
            max_distance_sets = [r]
        elif sum_distance == max_distance:
            max_distance_sets.append(r)

    return max_distance, max_distance_sets


# Input

filename = input("File Name: ")
start()

G = readcsv(filename)

v_num = G.number_of_nodes()
e_num = G.number_of_edges()
r_num = e_num - v_num + 1

# Array for storing minimal cycles
min_cycle = nx.minimum_cycle_basis(G)

# Array to store one selection of vertices from each minimal cycle
r_set = list(itertools.product(*min_cycle))

# Finding the maximum distance combination
max_distance, max_distance_sets = find_max_distance_set(G, r_set)
    
flag = 0

for r_set in max_distance_sets:
    i_max = 0
    d_max = 0
    sum_distance = 0
    
    i_max = r_set
     
    indeg = [1] * (v_num+1)
    for i in i_max:    
        indeg[i] = 2
    indeg[v_num] = -1
    v_color = ['lightblue' if indeg[i] == 1 else 'red' if indeg[i] == 2 else 'lightgreen' for i in range(v_num)]
     
    G_temp = nx.Graph()
    # N is an undirected graph, N2 is a directed graph
    N2 = nx.DiGraph()
    N = nx.Graph()
    N2.add_nodes_from(range(v_num + 1))
     
    for root_edge in G.edges():
        G_temp.clear()
        N.clear()
        N2.clear()
        N2.add_nodes_from(range(v_num + 1))
        G_temp = G.copy()
        N = orientation(G_temp, root_edge, v_num)
        G_temp.remove_edge(root_edge[0], root_edge[1])
         
        k = 0
        while k < v_num:
            k += 1
            for i in range(v_num):
                if N.degree(i) == indeg[i]:
                    for j in list(G_temp.neighbors(i)):
                        N.add_edge(i, j)
                        N2.add_edge(i, j)
                        G_temp.remove_edge(i, j)
        N2.add_edge(v_num, root_edge[0])
        N2.add_edge(v_num, root_edge[1])
         
        v_color = ['lightblue' if indeg[i] == 1 else 'red' if indeg[i] == 2 else 'lightgreen' for i in range(v_num + 1)]
          
        if nx.is_weakly_connected(N2):
            is_tree_child_result = all(is_tree_child(N2, indeg, l) for l in range(v_num + 1))
            if is_tree_child_result:
               end()
               flag = 1
               nx.draw(N2, pos=nx.kamada_kawai_layout(N), with_labels=True, node_size=100, font_size=8, arrows=True, node_color=v_color)
               plt.savefig(filename + '_algo2.pdf', format='pdf')  # Image format (here saved as pdf)
               plt.show()
               print("TC-Orientability: YES")
               break
    if flag == 1:
        break
if flag == 0: # If orientation not possible, output ‘Probably NO’.
    end()
    print("TC-Orientability: Probably NO")
