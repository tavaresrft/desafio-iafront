import numpy as np

from sklearn.cluster import KMeans
from sklearn.cluster import MiniBatchKMeans
from sklearn.cluster import AgglomerativeClustering
from sklearn.cluster import SpectralClustering
from sklearn.cluster import Birch

#cluster_list=[kmeans,mini_batch_kmeans,agglomerative_clustering,spectral_clustering,birch]
#cluster_names=['kmeans','mini_batch_kmeans','agglomerative_clustering','spectral_clustering','birch']

def kmeans(vector: np.array, n: int):
    k = KMeans(n_clusters=n, random_state=0)
    cluster_coordinate = k.fit_transform(vector)
    cluster_label = k.fit(vector)
    return cluster_label.labels_, cluster_coordinate 

def mini_batch_kmeans(vector: np.array, n: int):
    mbk = MiniBatchKMeans(n_clusters=n, random_state=0)
    cluster_coordinate = mbk.fit_transform(vector)
    cluster_label = mbk.fit(vector)
    return cluster_label.labels_, cluster_coordinate 

def agglomerative_clustering(vector: np.array, n: int):
    cluster = AgglomerativeClustering(n_clusters= n)
    cluster_label=cluster.fit(vector)
    return cluster_label.labels_

def spectral_clustering(vector: np.array, n: int):
    spc = SpectralClustering(n_clusters=n)
    cluster_label = spc.fit(vector)
    return cluster_label.labels_

def birch(vector: np.array, n: int):
    birch = Birch(n_clusters=n)
    cluster_label = birch.fit_predict(vector)
    return cluster_label
