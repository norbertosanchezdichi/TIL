# Import libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Import dataset
dataset = pd.read_csv('Social_Network_Ads.csv')
X = dataset.iloc[:, :-1].values
Y = dataset.iloc[:, -1].values

print(f"X = {X}")
print(f"Y = {Y}")
print()

# Split Dataset: Training Set and Test Set
from sklearn.model_selection import train_test_split
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size = 0.25, random_state = 0)

print(f"X_train = {X_train}")
print(f"X_test = {X_test}")
print(f"Y_train = {Y_train}")
print(f"Y_test = {Y_test}")
print()

# Feature Scaling (done after splitting to avoid information leakage.)
from sklearn.preprocessing import StandardScaler
standardScaler = StandardScaler()
X_train_scaled = standardScaler.fit_transform(X_train)
X_test_scaled = standardScaler.transform(X_test)

print(f"X_train_scaled = {X_train_scaled}")
print(f"X_test_scaled = {X_test_scaled}")
print()

# Random Forest Classifier
## Uses Ensemble Learning - leverages a number of Decision Tree models.
### 1. Pick at random K data points from the Training Set.
### 2. Build the Decision Tree associated to these K data points.
### 3. Choose the number N of trees to build and repeat steps 1 and 2.
### 4. For a new data point, make each one of your N trees predict the category.  Assign the new data point to the category that wins the majority vote.
## Gives better predictive power than Decision Trees.
## It does not give the same intrepability as a Decision Tree.  You cannot do the same with a Random Forest.
## To find the optimal number of Decision Trees, use k-Fold Cross Validation and Grid Search.
