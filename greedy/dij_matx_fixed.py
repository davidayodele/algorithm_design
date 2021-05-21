'''
References:
https://www.geeksforgeeks.org/printing-paths-dijkstras-shortest-path-algorithm/
https://www.youtube.com/watch?v=zFnmPyXDk_A
https://algorithms.tutorialhorizon.com/djkstras-shortest-path-algorithm-adjacency-matrix-java-code/#:~:text=Menu-,Dijkstra%27s%20–%20Shortest%20Path%20Algorithm%20(SPT,)%20–%20Adjacency%20Matrix%20–%20Java%20Implementation&text=For%20a%20given%20source%20node,node%20and%20every%20other%20node.
'''
import pandas as pd
import sys
import os
import csv
import numpy as np
import matplotlib.pyplot as plt
from IPython.display import display
import time
import io
from io import StringIO


# ============ Dijkstra's Implementation ==============

class Network:

    def __init__(self, net, nodes):
        self.vertices = nodes
        self.graph = net   # [[0 for column in range(nodes)] for row in range(nodes)]

    # finds nearest vertex not yet visited
    def minDistance(self, visited, dist):
        min = INT_MAX # initialize min dist of next node
        min_index = -1

        for v in range(self.vertices): # search for vertex not in visited
            if visited[v] == False and min > dist[v]:
                min = dist[v]
                min_index = v
        return min_index

    def printSPT(self, src, dist, paths):
        for v in range(self.vertices):
            #paths[v] = list(set(paths[v][2:]))
            print("source: " + str(src) + ", to node: " + str(v) + ", distance: " + str(dist[v]) + ", path: ")
            self.printPath(paths, v)
            print("===================")

    def printPath(self, parent, j):
        #base case : if j is source, recursively prints most recently added item in parent
        if parent[j] == -1: 
            print(j)
            return
        self.printPath(parent , parent[j])
        print(j)
    
    # Implements Dijkstra's using adjacency matrix
    def dijkstra(self, src):
        dist = [INT_MAX] * self.vertices
        #dist = [INT_MAX for item in range(self.vertices)]
        dist[src] = 0 # Distance of source vertex from itself is always 0
        visited = [False] * self.vertices
        parent = [-1] * self.vertices # list to store path

        # build SPT
        for node in range(self.vertices):
          path = []
          # Picks the vertex at minimum distance in set of vertices not yet visited
          # v_min is src in 1st iteration
          v_min = self.minDistance(visited, dist)

          # Puts minimum distance vertex in visited list
          visited[v_min] = True
          path.append(v_min)

          # Updates dist value of the adjacent vertices (when current dist > new dist and vertex is not in SPT
          for v in range(self.vertices):
            if self.graph[v_min][v] > 0:
                if(visited[v] == False and self.graph[v_min][v] != INT_MAX): # dist[v] > dist[u]
                  # check if dist needs update (i.e. tot weight from src to v is < current dist)
                  new_min = self.graph[v_min][v] + dist[v_min]

                  if (new_min < dist[v]):
                    dist[v] = new_min
                    parent[v] = v_min

        self.printSPT(src, dist, parent)

# ============ End Dijkstra's Implementation ==============


# ============ Converts CSV data to Adjacency Matrix ==============

def csv_to_matx(csv_data):
    matx = []
    matx_row = []
    max_len = max(np.max(csv_data[:, 0], 0), np.max(csv_data[:, 1], 0)) # get the max val in the link or source col (will be final matx col and row dimensions)
    INIT_VAL = 0
    data_rows = np.shape(csv_data)[0]

    matx = [ [ INIT_VAL for col in range(max_len) ] for row in range(max_len) ]

    matx = pd.DataFrame(matx)
    #display(matx)     
     
    row = 0
    matx_rows = len(matx)      
    for matx_row in range(matx_rows):
        while row < data_rows and (csv_data[row, 0] == matx_row):
            link = csv_data[row, 1]
            weight = csv_data[row, 2]
            #print(link)
            #print(weight) # will be used as col index
            matx[matx_row][link] = weight
            row = row + 1
    matx = np.array(matx)
    return matx, max_len

# ============ End Converts CSV data to Adjacency Matrix ==============


# Main

# from google.colab import drive
# drive.mount("/content/gdrive")

# starting time
start = time.time()

# data_path = 'project2/Project2_Input_Files/Project2_Input_File3.csv'
# data_path = '/content/gdrive/My Drive/Colab Notebooks/2591_proj2/Project2_Input_File3.csv'
data_path = 'copied_raw_github_link'
data = pd.read_csv(data_path, usecols=['NodeID','ConnectedNodeID','Distance']) # 'Coordinates', 'Intersection_Name'
#print(data)
data = np.asarray(data)
#data_small = data[0:9,:] # 1st 10 rows only

matx, max_len = csv_to_matx(data)
INT_MAX = 999999

# ========== File output ===================
# old_stdout = sys.stdout
# new_stdout = io.StringIO()
# sys.stdout = new_stdout

# file1 = open("project2/dij_matx_correct_path_187.txt","a")
# file1 = open("/content/gdrive/My Drive/Colab Notebooks/2591_proj2/dij_matx_correct_path_187.txt","a")
# ==========================================

net = Network(matx, max_len)
net.dijkstra(187)

# end time
end = time.time()
print("Runtime of the program is : " + str(end - start))

# ========== File output ===================
# output = new_stdout.getvalue()
# file1.write(output)

# file1.close()
# sys.stdout = old_stdout
# ==========================================