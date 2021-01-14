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

# Feature Scaling (done after splitting to avoid information leakage)
## Feature scaling also done for dependent variable so as to not neglect them in the model
## X_train and Y_train both have a different mean and standard deviation and so they require their own scale
from sklearn.preprocessing import StandardScaler
standardScaler_X = StandardScaler()
standardScaler_Y = StandardScaler()
X_train_scaled = standardScaler_X.fit_transform(X_train)
Y_train_scaled = standardScaler_Y.fit_transform(Y_train)

print(f"X_train_scaled = {X_train_scaled}")
print(f"Y_train_scaled = {Y_train_scaled}")
print()

# The Nature of Statistical Learning Theory by Vladimir Vapnik
# ε-Insensitive Tube is a margin of error in SVR that is allowed for the model.
# Slack Variables ζ1* (below ε-Insensitive Tube) and ζ2 (above ε-Insensitive Tube) are used to calculate error.
## The Slack Variables are the support vectors that form the structure of the ε-Insensitive Tube.

# Create and Train Support Vector Regression (SVR) Model
# Use The Gaussian Radial Basis Function (RBF) Kernel
## Other kernels are Polynomial, Gaussian, Laplace RBF, Hyperbolic Tangent, Sigmoid, Bessel Function of First Kind, Anova RB, and Linear Spline in 1D
from sklearn.svm import SVR
regressor = SVR(kernel = 'rbf')
regressor.fit(X_train_scaled, Y_train_scaled.ravel())

# Predict using Support Vector Regression
Y_predict = standardScaler_Y.inverse_transform(regressor.predict(standardScaler_X.transform(X_test)))

# Output Training and Test Set results
np.set_printoptions(precision = 2)
print(f"[Y_predict Y_test] = {np.concatenate((Y_predict.reshape(len(Y_predict), 1), Y_test.reshape(len(Y_test), 1)), axis = 1)}")
print()

# Evaluate Model Performance
from sklearn.metrics import r2_score
print(f"R2 Score = {r2_score(Y_test, Y_predict)}")

print(f"Adusted R2 Score = {1 - (1 - r2_score(Y_test, Y_predict)) * ((len(X_test) - 1) / (len(X_test) - len(X_test[0]) - 1))}")
