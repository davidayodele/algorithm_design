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
        clusters = [[] for count in range(self.K)] # init empty clusters

    
    def calc_centroids(self, clusters, data):
        pass

    def guess_cluster(self, clusters, data):
        pass

    def plot_fig(self, x_data, y_data):
        pass

    def fit(self, data):
        pass


    