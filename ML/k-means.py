import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
from matplotlib.pyplot import figure

from sklearn.datasets import make_blobs
data, labels = make_blobs(n_samples=500, centers=3, n_features=2, random_state=20)


def init_centroids(k, data):
    rand_points = []
    for i in range(k):
        x1 = np.random.uniform(min(data[:, 0]), max(data[:, 0]))  # generates a random x-coord
        x2 = np.random.uniform(min(data[:, 1]), max(data[:, 1]))  # generates a random y-coord
        rand_points.append([x1, x2])

    return np.array(rand_points) # will return an array of K points with x & y coords

def euc_dist(x, y):
    return np.sqrt(sum(np.square(x - y))) # calculates euclidiean distance between 2 points

def assign_cluster(k_val, data, centroids):
    points = len(data)
    clusters = [0] * points # init an array of cluster assignments for each data point
    for pt in range(points):
        cluster_distances = []
        for k in range(k_val):
            cluster_distances.append(euc_dist(data[pt], centroids[k])) # calc point-centroid distance, looping through centroids 1st, then pts
        nearest_centroid = np.argmin(cluster_distances) # finds index of closest centroid (before going to next pt) 
        clusters[pt] = nearest_centroid # assigns nearest centroid to clusters array for this point 
    
    return np.asarray(clusters)


def find_centroids(k_val, data, clusters):
    points = len(data)
    centroids = []
    for k in range(k_val):
        cluster = []  # for each k, make a cluster array to store nearest pts
        for pt in range(points):
            if clusters[pt] == k:
                cluster.append(data[pt]) # add point to cluster array if it is assigned to this k
        centroids.append(np.mean(cluster, axis=0)) # find the center(geometric mean) of the cluster and add it to centroids array
    return np.asarray(centroids)

def centroid_change(old_centroids, new_centroids):
    distance = 0
    for pt1, pt2 in zip(old_centroids, new_centroids):
        distance += euc_dist(pt1, pt2) # add up distances betweeen all points
    return distance 


def show_clusters(data, cluster, centroids):
    df = pd.DataFrame(dict(x=data[:, 0], y=data[:, 1], label=cluster))
    colors = {0:'blue', 1:'yellow', 2:'green'}
    fig, axis = plt.subplots(figsize=(8, 8))
    grouped = df.groupby('label')

    for key, group in grouped:
        group.plot(ax=axis, kind='scatter', x='x', y='y', label=key, color=colors[key])
    
    axis.scatter(centroids[:, 0], centroids[:, 1], marker='*', s=150, c='#ff0000')
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.show()

            
def k_means(k_val, data):
    points = len(data)
    old_centroids = init_centroids(k_val, data)
    cluster = [0] * points
    centroid_diff = 100
    
    while centroid_diff > 0.001:
        cluster = assign_cluster(k_val, data, old_centroids)
        show_clusters(data, cluster, old_centroids)
        new_centroids = find_centroids(k_val, data, cluster)
        centroid_diff = centroid_change(new_centroids, old_centroids)
        old_centroids = new_centroids

    return cluster



# Main
 
cluster = k_means(3, data)



    