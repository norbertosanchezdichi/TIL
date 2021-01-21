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

# Split Dataset: Training Set and Test Set
from sklearn.model_selection import train_test_split
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size = 0.2, random_state = 0)

print(f"X_train = {X_train}")
print(f"X_test = {X_test}")
print(f"Y_train = {Y_train}")
print(f"Y_test = {Y_test}")
print()

# Simple Linear Regressor
## The squared differences are calculated instead of the absolute differences because it makes the calculation of the first derivative of the loss error function easier.
## Feature Scaling is not required because the prediction is a simple linear combination where the coefficients can adapt their scale to put everything on the same scale.
## Understanding the P-Value
### The Null Hypothesis is the assumption that the parameters associated to the independent variables are equal to zero.
#### Under this assumption, the observations are random and don't follow a certain pattern.
### The P-Value is the probability that the parameters associated to the independent variables have certain nonzero values given that the Null Hypothesis is true.
### The P-Value is a statistical metric: the lower its value, the more statistically significant is an independent variable (how much better a predictor it will be).

# Create and train the Simple Linear Regression model
from sklearn.linear_model import LinearRegression
regressor = LinearRegression()
regressor.fit(X_train, Y_train)

# Predict using Linear Regression
Y_predict = regressor.predict(X_test)

# Output Training and Test Set results
np.set_printoptions(precision = 2)
print(f"[Y_predict Y_test] = {np.concatenate((Y_predict.reshape(len(Y_predict), 1), Y_test.reshape(len(Y_test), 1)), axis = 1)}")
print()

# Print multiple linear regressor coefficient and intercept.
print(f"Coefficients = {regressor.coef_}")
print(f"Intercept = {regressor.intercept_}")
print()

# Evaluate Model Performance
from sklearn.metrics import r2_score
print(f"R2 Score = {r2_score(Y_test, Y_predict)}")

print(f"Adusted R2 Score = {1 - (1 - r2_score(Y_test, Y_predict)) * ((len(X_test) - 1) / (len(X_test) - len(X_test[0]) - 1))}")
