'''
Implement Prim's algorithm to find and print a minimum-spanning tree of a given network

References:
https://www.geeksforgeeks.org/prims-algorithm-simple-implementation-for-adjacency-matrix-representation/
'''

import csv
import os

datafile = 'quiz6/Quiz6_Input_File.csv'

data = list(csv.reader(open(datafile)))

from sys import maxsize
INT_MAX = maxsize
V = 5


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

    matx = [[0]*(len(data) - 2) for col in range(len(data[0]))]

    for row in data:
        for col in row:
            for index, val in enumerate(matx):
                while col == index:
                    matx[col] = val 
    print(matx)
    # Print the solution

    prim(cost)

    #cwd = os.getcwd()
    #print(cwd)
    print(data[1][4])
