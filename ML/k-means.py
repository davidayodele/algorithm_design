import numpy as np



class k_means:
    def __init__(self, data, K):
        self.K = K
        self.plot_figure = True
        self.max_iters = 100
        self.num_points, self.num_features = data.shape

    def init_centroids(self, data):
        centroids = np.zeros((self.K, self.num_features))

        for count in range (self.K):
            centroid = data[np.random.choice(range(self.num_points))]
            centroids[count] = centroid

        return centroids

    def make_clusters(self, data, centroids):
        clusters = [[] for cluster in range(self.K)] # init empty array of clusters
        # the number of arrays embedded in the outer array will depend on K
        
        for idx, point in enumerate(data): # each point will be a 2-tuple
            # data has 3 cols (X, Y, Feature)
            centroid_distances = np.sqrt(np.sum( (point - centroids)**2, axis=1) ) # creates Kx2 array of point-centroid distances
            # numpy will take each point (X,Y) then subtract it from each centroid, then square the result, then sum the y vals (axis=1). 
            # We then loop to next point
            
            nearest_centroid = np.argmin(centroid_distances)
    
    def calc_centroids(self, clusters, data):
        pass

    def guess_cluster(self, clusters, data):
        pass

    def plot_fig(self, x_data, y_data):
        pass

    def fit(self, data):
        pass


    