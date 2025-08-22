# Ejercicio 3 Scikit-learn: Clustering con KMeans
from sklearn.cluster import KMeans
import numpy as np

X = np.array([[1, 2], [1, 4], [1, 0], [4, 2], [4, 4], [4, 0]])

kmeans = KMeans(n_clusters=2, random_state=0)
kmeans.fit(X)

print('Centros de los clusters:', kmeans.cluster_centers_)
print('Etiquetas de los puntos:', kmeans.labels_)
