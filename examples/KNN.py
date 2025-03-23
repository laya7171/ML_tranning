import numpy as np
from sklearn import datasets
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from supervised_learning.KNN.knn import KNN  # Ensure this path is correct

# Define a colormap for visualization
cmap = ListedColormap(['#FF0000', '#00FF00', '#0000FF'])

# Load the Iris dataset
iris = datasets.load_iris()
X, y = iris.data, iris.target

# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=1234)

# Visualize the dataset
plt.figure()
plt.scatter(X[:, 0], X[:, 1], c=y, cmap=cmap, edgecolor='k', s=20)
plt.xlabel('Sepal Length')
plt.ylabel('Sepal Width')
plt.show()

# Initialize and train the KNN classifier
clf = KNN(k=3)
clf.fit(X_train, y_train)

# Make predictions
predictions = clf.predict(X_test)
print("Predictions:", predictions)

# Calculate accuracy
acc = np.sum(predictions == y_test) / len(y_test)
print("Accuracy:", acc)