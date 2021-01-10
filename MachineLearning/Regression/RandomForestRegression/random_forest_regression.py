# Import libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Import dataset
dataset = pd.read_csv('Position_Salaries.csv')
X = dataset.iloc[:, :-1].values
Y = dataset.iloc[:, -1].values

print(f"X = {X}")
print(f"Y = {Y}")
print()

# Split Dataset: Training Set and Test Set
X_train = X[:, 1:2]
Y_train = Y

print(f"X_train = {X_train}")
print(f"Y_train = {Y_train}")
print()

# Random Forest Regression uses ensemble learning
## 1. Pick random K data points from Training Set.
## 2. Build the Decision Tree associated with these K points.
## 3. Choose the number N of trees to build and repeat #1 and #2
## 4.  For a new data point, make each one of your N trees predict the value for the point in question.  The new predicted output is the average across all the predicted N values.

# Create and Train Random Forest Regression Model
from sklearn.ensemble import RandomForestRegressor
regressor = RandomForestRegressor(n_estimators = 10, random_state = 0)
regressor.fit(X_train, Y_train)
