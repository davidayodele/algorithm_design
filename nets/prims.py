'''
Implement Prim's algorithm to find and print a minimum-spanning tree of a given network

References:
https://www.geeksforgeeks.org/prims-algorithm-simple-implementation-for-adjacency-matrix-representation/
'''

import csv
import os
from sys import maxsize

datafile = 'quiz6/Quiz6_Input_File.csv'

data = list(csv.reader(open(datafile)))

INT_MAX = maxsize

#V = 5
#V = len(data)

# Returns true if edge u-v is a valid edge to be
# include in MST. An edge is valid if one end is
# already included in MST and other is not in MST.

def is_edge(u, v, MST):
    if u == v:
        return False
    if MST[u] == False and MST[v] == False:
        return False
    elif MST[u] == True and MST[v] == True:
        return False
    return True


def prim(cost):
    V = len(cost)
    MST = [False] * V

    # Initialize at 0
    MST[0] = True

    #Adds edges until number of edges is V-1.
    edge_count = 0
    min_cost = 0
    while edge_count < V - 1:

        # Finds min edge weight.
        min_wt = INT_MAX
        a = -1
        b = -1
        for i in range(V):
            for j in range(V):
                if cost[i][j] < min_wt:
                    if is_edge(i, j, MST):
                        min_wt = cost[i][j]
                        a = i
                        b = j

        if a != -1 and b != -1:
            print 'Edge %d: (%d, %d) cost: %d' % (edge_count, a, b,
                    min_wt)
            edge_count += 1
            min_cost += min_wt
            MST[b] = MST[a] = True

    print 'Minimum cost = %d' % min_cost

# Main
if __name__ == '__main__':

    cost = [[INT_MAX, 2, INT_MAX, 6, INT_MAX], 
            [2, INT_MAX, 3, 8, 5],
            [INT_MAX, 3, INT_MAX, INT_MAX, 7], 
            [6, 8, INT_MAX, INT_MAX, 9], 
            [INT_MAX, 5, 7, 9, INT_MAX]]

    matx = []
    matx_col = []

    for col in range(1, len(data)): # initialize column with 0s, must be length of data col
            matx_col.append(INT_MAX) # change to 0 for Dij
    for row in range(0, len(data[0]) - 2): # append the column to each row, only need idices & weight
        matx.append(matx_col)
            
    row = 1  # avoid header row    
    for matx_row in range(len(matx)):
        while int(data[row][0]) == matx_row:
            link = int(data[row][1])
            weight = int(data[row][2])
            #print(link)
            #print(weight) # will be used as col index
            matx[matx_row][link] = weight
            row = row + 1

    # Print the matrix/list                        
    print(matx)
    
    
    # Print the solution
    #prim(cost)
    prim(matx)

    #cwd = os.getcwd()
    #print(cwd)
    #print(data[1][0])
    #print(matx[1][1])

