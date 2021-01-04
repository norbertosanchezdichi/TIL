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

# Train Linear Regression model on Training Set
from sklearn.linear_model import LinearRegression
linearRegressor = LinearRegression()
linearRegressor.fit(X_train, Y_train)

# Train Polynomial Regression model on Training Set
from sklearn.preprocessing import PolynomialFeatures
polynomialPreprocessor = PolynomialFeatures(degree = 2)
X_polynomial = polynomialPreprocessor.fit_transform(X_train)

linearRegressor_polynomial = LinearRegression()
linearRegressor_polynomial.fit(X_polynomial, Y)