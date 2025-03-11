from __future__ import division, print_function
from sklearn import datasets
import numpy as np
import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from unsupervised_learning.k_means_clusturing.k_means_clusturing import KMeans

import matplotlib
matplotlib.use('Agg')  # Use Agg backend for saving to file
import matplotlib.pyplot as plt

def main():
  X,y = datasets.make_blobs()
  
  clf = KMeans(k=3)
  y_pred= clf.predict(X)
  
  #Plotting figure
  
  plt.figure(figsize = (10,8))
  plt.scatter(X[:,0],X[:,1],c=y_pred, cmap='viridis')
  plt.title("KMeans Clustering")
  plt.xlabel("X")
  plt.ylabel("Y")
  plt.savefig('examples/k_means.png')
  print("Plot has been saved as k_means.png")
  
if __name__ == "__main__":
  main()
