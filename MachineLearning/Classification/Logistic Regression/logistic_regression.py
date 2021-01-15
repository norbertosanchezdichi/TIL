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

# Logistic Regression
## Using the Sigmoid Function with Euler's number, solving for the dependent variable 'Y' in terms of the probability allows to model the solution with a linear equation.
## The solution is in terms of probability using the natural log - hence why it is called Logistic Regression.
# Assumptions when using Logistic Regression
## 1. Binary Logistic Regreesion requires the dependent variable to be binary. Ordinal Logistic Regression requires the dependent variable to be ordinal.
## 2. Requires the observations to be independent of each other.
## 3. Requires little or no multicollinearity among the independent variables.
## 4. Requires that the independent variables are linearly related to the log odds.
