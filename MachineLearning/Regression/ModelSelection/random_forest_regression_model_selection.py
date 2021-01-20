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

# Random Forest Regression uses ensemble learning
# A Random Forest Regression model has better predictability compared to a Decision Tree Regression Model.  However, it has less interpretability.

## 1. Pick random K data points from Training Set.
## 2. Build the Decision Tree associated with these K points.
## 3. Choose the number N of trees to build and repeat #1 and #2
## 4.  For a new data point, make each one of your N trees predict the value for the point in question.  The new predicted output is the average across all the predicted N values.

# Create and train the Random Forest Regression model
## Use 10 trees in the forest
from sklearn.ensemble import RandomForestRegressor
regressor = RandomForestRegressor(n_estimators = 10, random_state = 0)
regressor.fit(X_train, Y_train.ravel())

# Predict using Random Forest Regression
Y_predict = regressor.predict(X_test)

# Output Training and Test Set results
np.set_printoptions(precision = 2)
print(f"[Y_predict Y_test] = {np.concatenate((Y_predict.reshape(len(Y_predict), 1), Y_test.reshape(len(Y_test), 1)), axis = 1)}")
print()

# Evaluate Model Performance
from sklearn.metrics import r2_score
print(f"R2 Score = {r2_score(Y_test, Y_predict)}")

print(f"Adusted R2 Score = {1 - (1 - r2_score(Y_test, Y_predict)) * ((len(X_test) - 1) / (len(X_test) - len(X_test[0]) - 1))}")
