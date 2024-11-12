import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns 
from scipy import stats

#load the dataset into pandas 
data = pd.read_csv("Desktop/iris.csv")


#display the description and the information of the data
print("discription")
print(data.describe(include = 'all'))
print("information")
print(data.info())


#display the intial values 
print(data.head())
print(data)


#find the missing values and handle them 
missing_values = data.isnull().sum()
print(missing_values)
data = data.dropna(subset=['species'])
numeric_cols = ["sepal_length","sepal_width","petal_length","petal_width"]
for col in numeric_cols:
  data[col].fillna(data[col].median(),inplace = True)



#outliers
for col in numeric_cols:
  q1 = data[col].quantile(0.25)
  q3 = data[col].quantile(0.75)
  iqr = q3 - q1
  lower_bound = q1 - 1.5 * iqr
  upper_bound = q3 + 1.5 * iqr
  outliers = data[(data[col] < lower_bound) | (data[col] > upper_bound)]
  print(outliers)

#data transformation
plt.figure(figsize = (10,5))
sns.histplot(data['sepal_length'], kde=True)
plt.title('Original Distribution of Sepal Length')
plt.xlabel('Sepal Length')
plt.ylabel('Frequency')
plt.show()

data['sepal_length_log'] = np.log1p(data['sepal_length'])


plt.figure(figsize=(10, 5))
sns.histplot(data['sepal_length_log'], kde=True)
plt.title('Log-Transformed Distribution of Sepal Length')
plt.xlabel('Log of Sepal Length')
plt.ylabel('Frequency')
plt.show()



#catogorical into quntitive
data = pd.read_csv('Desktop/iris.csv')
print("Unique values in 'species':", data['species'].unique())
data_encoded = pd.get_dummies(data, columns=['species'], drop_first=True)
print("\nDataset after one-hot encoding 'species':\n", data_encoded.head())
#load the dataset into pandas 
data = pd.read_csv("Desktop/iris.csv")


#display the description and the information of the data
print("discription")
print(data.describe(include = 'all'))
print("information")
print(data.info())


#display the intial values 
print(data.head())
print(data)


#find the missing values and handle them 
missing_values = data.isnull().sum()
print(missing_values)
data = data.dropna(subset=['species'])
numeric_cols = ["sepal_length","sepal_width","petal_length","petal_width"]
for col in numeric_cols:
  data[col].fillna(data[col].median(),inplace = True)



#outliers
for col in numeric_cols:
  q1 = data[col].quantile(0.25)
  q3 = data[col].quantile(0.75)
  iqr = q3 - q1
  lower_bound = q1 - 1.5 * iqr
  upper_bound = q3 + 1.5 * iqr
  outliers = data[(data[col] < lower_bound) | (data[col] > upper_bound)]
  print(outliers)

#data transformation
plt.figure(figsize = (10,5))
sns.histplot(data['sepal_length'], kde=True)
plt.title('Original Distribution of Sepal Length')
plt.xlabel('Sepal Length')
plt.ylabel('Frequency')
plt.show()

data['sepal_length_log'] = np.log1p(data['sepal_length'])


plt.figure(figsize=(10, 5))
sns.histplot(data['sepal_length_log'], kde=True)
plt.title('Log-Transformed Distribution of Sepal Length')
plt.xlabel('Log of Sepal Length')
plt.ylabel('Frequency')
plt.show()



#catogorical into quntitive
data = pd.read_csv("Desktop/iris.csv")
print("Unique values in 'species':", data['species'].unique())
data_encoded = pd.get_dummies(data, columns=['species'], drop_first=True)
print("\nDataset after one-hot encoding 'species':\n", data_encoded.head())