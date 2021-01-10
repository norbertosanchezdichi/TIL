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

# Decision Trees
## Two types: Classification Trees and Regression Trees
# Splits or 'terminal leaves' are created if they provide new useful information about the data set
# No feature scaling is required because the splitting of data does not require it

# Create and Train Decision Tree Regression Model
from sklearn.tree import DecisionTreeRegressor
regressor = DecisionTreeRegressor(random_state = 0)
regressor.fit(X_train, Y_train)
