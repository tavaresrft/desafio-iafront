import numpy as np
from sklearn.cluster import KMeans


def kmeans(vector: np.array, n: int):
    k = KMeans(n_clusters=n, random_state=0)
    cluster_coordinate = k.fit_transform(vector)
    cluster_label = k.fit(vector)

    return cluster_coordinate, cluster_label.labels_
