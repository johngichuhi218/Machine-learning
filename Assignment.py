# -*- coding: utf-8 -*-
"""Untitled2.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1ip1GXBqWyshl8Ww2dMZWrFvNJJZ91Yng
"""

import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, mean_absolute_error

# Assuming you have a dataset with features and target variable
# Let's say your dataset is in a CSV file named 'house_data.csv'
# Replace 'house_data.csv' with your actual dataset file
# Assume the target variable is 'price'

# Load the dataset
data = pd.read_csv('/content/sample_data/Real estate.csv')

# Assuming 'price' is the target variable
X = data.drop('Y house price of unit area', axis=1)  # Features
y = data['Y house price of unit area']  # Target variable

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Create and train the linear regression model
model = LinearRegression()
model.fit(X_train, y_train)

# Make predictions on the testing set
predictions = model.predict(X_test)

# Calculate evaluation metrics
mse = mean_squared_error(y_test, predictions)
mae = mean_absolute_error(y_test, predictions)
rmse = np.sqrt(mse)

print("Mean Squared Error (MSE):", mse)
print("Mean Absolute Error (MAE):", mae)
print("Root Mean Squared Error (RMSE):", rmse)

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
data = pd.read_csv('/content/sample_data/Real estate.csv')

# Display the first few rows of the dataset
print("First few rows of the dataset:")
print(data.head())

# Summary statistics of numerical features
print("\nSummary statistics of numerical features:")
print(data.describe())

# Check for missing values
print("\nMissing values in the dataset:")
print(data.isnull().sum())

# Visualize the distribution of the target variable 'price'
plt.figure(figsize=(10, 6))
sns.histplot(data['Y house price of unit area'], kde=True, color='blue', bins=30)
plt.title('Distribution of House Prices')
plt.xlabel('Price')
plt.ylabel('Frequency')
plt.show()

# Correlation matrix heatmap
plt.figure(figsize=(12, 8))
sns.heatmap(data.corr(), annot=True, cmap='coolwarm', fmt=".2f")
plt.title('Correlation Matrix Heatmap')
plt.show()

# Pairplot for visualizing relationships between numerical features
sns.pairplot(data)
plt.title('Pairplot of Numerical Features')
plt.show()