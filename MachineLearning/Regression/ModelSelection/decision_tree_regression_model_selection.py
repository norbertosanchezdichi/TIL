# Import libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Import dataset
dataset = pd.read_csv('Data.csv')
X = dataset.iloc[:, :-1].values
Y = dataset.iloc[:, -1].values

print(f"X = {X}")
print(f"Y = {Y}")
print()

# Convert Y to 2D Array for Feature Scaling
Y = Y.reshape(len(Y), 1)

print(f"Y as a 2D array = {Y}")
print()

# Split Dataset: Training Set and Test Set
from sklearn.model_selection import train_test_split
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size = 0.2, random_state = 0)

print(f"X_train = {X_train}")
print(f"X_test = {X_test}")
print(f"Y_train = {Y_train}")
print(f"Y_test = {Y_test}")
print()

# Decision Trees
## Two types: Classification Trees and Regression Trees
# Splits or 'terminal leaves' are created if they holistically reduce the standard deviation of the predictions
# The Information Gain is the Standard Deviation Reduction.  The more the standard deviation decreases, the less the entropy and the more homogenous the child nodes become
# No feature scaling is required because the splitting of data does not require it

# Create and train the Decision Tree Regression model
from sklearn.tree import DecisionTreeRegressor
regressor = DecisionTreeRegressor(random_state = 0)
regressor.fit(X_train, Y_train)

# Predict using Decision Tree Regression
Y_predict = regressor.predict(X_test)

# Output Training and Test Set results
np.set_printoptions(precision = 2)
print(f"[Y_predict Y_test] = {np.concatenate((Y_predict.reshape(len(Y_predict), 1), Y_test.reshape(len(Y_test), 1)), axis = 1)}")
print()

# Evaluate Model Performance
from sklearn.metrics import r2_score
print(f"R2 Score = {r2_score(Y_test, Y_predict)}")

print(f"Adusted R2 Score = {1 - (1 - r2_score(Y_test, Y_predict)) * ((len(X_test) - 1) / (len(X_test) - len(X_test[0]) - 1))}")
