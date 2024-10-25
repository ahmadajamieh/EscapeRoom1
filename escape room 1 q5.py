import numpy as np

#Room 5: Unsupervised Learning - Clustering

data = [3.1, 2.9, 5.4, 6.2, 1.9, 5.7]
threshold = 3.5

cluster_1 = [x for x in data if x <= threshold]  
cluster_2 = [x for x in data if x > threshold]  

print(f"Cluster 1: {cluster_1}")
print(f"Cluster 2: {cluster_2}")