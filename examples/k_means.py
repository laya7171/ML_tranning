from sklearn import datasets
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

def main():
    # Generate synthetic data
    X, y = datasets.make_blobs(n_samples=300, centers=3, random_state=42)

    # Apply K-Means Clustering
    kmeans = KMeans(n_clusters=3, n_init=10, random_state=42)
    kmeans.fit(X)
    y_pred = kmeans.predict(X)

    # Plot results
    plt.figure(figsize=(10, 8))
    plt.scatter(X[:, 0], X[:, 1], c=y_pred, cmap='viridis', alpha=0.7)
    plt.scatter(kmeans.cluster_centers_[:, 0], kmeans.cluster_centers_[:, 1], 
                c='red', marker='X', s=200, label="Cluster Centers")  # Mark cluster centers
    plt.title("K-Means Clustering")
    plt.xlabel("Feature 1")
    plt.ylabel("Feature 2")
    plt.legend()

    # Save the figure
    save_path = "k_means2.png"  # Adjust path if needed
    plt.savefig(save_path)
    print(f"Plot has been saved as {save_path}")

if __name__ == "__main__":
    main()
