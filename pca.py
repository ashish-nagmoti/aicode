import pandas as pd
import numpy as np
from sklearn.datasets import load_iris
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt
import seaborn as sns


iris = load_iris()
data = pd.DataFrame(data=iris.data, columns=iris.feature_names)
target = iris.target

print("Dataset preview:\n", data.head())

scaler = StandardScaler()
data_scaled = scaler.fit_transform(data)


pca = PCA(n_components=2)
principal_components = pca.fit_transform(data_scaled)


pca_data = pd.DataFrame(data=principal_components, columns=['PC1', 'PC2'])
pca_data['Target'] = target


plt.figure(figsize=(10, 6))
sns.scatterplot(x='PC1', y='PC2', hue='Target', palette='viridis', data=pca_data)
plt.title("PCA of Iris Dataset")
plt.xlabel("Principal Component 1")
plt.ylabel("Principal Component 2")
plt.show()


explained_variance = pca.explained_variance_ratio_
print("Explained Variance Ratio of each Principal Component:", explained_variance)
print("Total Explained Variance (2 components):", explained_variance.sum())