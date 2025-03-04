from utils import euclidean_distance

class KMeans():
  
  def __init__(self,k=2, max_iteration = 500):
    self.k = k
    self.max_iterations = max_iteration
    
  def _init_random_centroids(self,X):
    n_samples, n_feature = np.shape()
    centroids = np.zeros((self.k,n_feature))
    for i in range(self.k):
      centroid = X[np.random.choice(range(n_samples))]
      centroids[i] = centroid
    return centroids
  
  def _closest_centroid(self,sample,centroids):
    closest_i = 0
    closest_dist = float('inf')
    for i, centroid in enumerate(centroids):
      distance = euclidean_distance(sample,centroid)
      if distance < closest_dist:
        closest_i = i
        closest_dist = distance
    