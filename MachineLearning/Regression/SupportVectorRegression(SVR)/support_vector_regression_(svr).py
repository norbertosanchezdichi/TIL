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

# Convert Y_train to 2D Array
Y_train = Y_train.reshape(len(Y_train), 1)

print(f"Y_train as a 2D array = {Y_train}")
print()

# Feature Scaling (done after splitting to avoid information leakage)
## Feature scaling also done for dependent variable so as to not neglect them in the model.
## X_train and Y_train both have a different mean and standard deviation and so they require their own scale.
## Feature Selection using P-Values to find most significant variables is not possible because SVR is a non-linear model. However, Feature Extraction is possible using Dimensionality Reduction.
from sklearn.preprocessing import StandardScaler
standardScaler_X = StandardScaler()
standardScaler_Y = StandardScaler()
X_train_scaled = standardScaler_X.fit_transform(X_train)
Y_train_scaled = standardScaler_Y.fit_transform(Y_train)

print(f"X_train_scaled = {X_train_scaled}")
print(f"Y_train_scaled = {Y_train_scaled}")
print()

# Support Vector Regression (SVR)
## The Nature of Statistical Learning Theory by Vladimir Vapnik
## ε-Insensitive Tube is a margin of error in SVR that is allowed for the model.
## Slack Variables ζ1* (below ε-Insensitive Tube) and ζ2 (above ε-Insensitive Tube) are used to calculate error.
### The Slack Variables are the support vectors that form the structure of the ε-Insensitive Tube.
# Create and train Support Vector Regression (SVR) model
## Use The Gaussian Radial Basis Function (RBF) Kernel
## Other kernels are Polynomial, Gaussian, Laplace RBF, Hyperbolic Tangent, Sigmoid, Bessel Function of First Kind, Anova RB, and Linear Spline in 1D

# Create and train Support Vector Regression (SVR) model
## Use the Gaussian Radial-Basis Function (RBF)
from sklearn.svm import SVR
regressor = SVR(kernel = 'rbf')
regressor.fit(X_train_scaled, Y_train_scaled.ravel())

# Predict salary for a 6.5 level position
Y_predict = standardScaler_Y.inverse_transform(regressor.predict(standardScaler_X.transform([[6.5]])))

# Output prediction salary for a position 6
print(f"Salary for a position 6.5 is = {Y_predict}")

# Output Support Vector Regression Results
plt.scatter(standardScaler_X.inverse_transform(X_train_scaled), standardScaler_Y.inverse_transform(Y_train_scaled), color = 'red')
plt.plot(standardScaler_X.inverse_transform(X_train_scaled), standardScaler_Y.inverse_transform(regressor.predict(X_train_scaled)), color = 'blue')
plt.title('Support Vector Regression Model')
plt.xlabel('Position Level')
plt.ylabel('Salary')
plt.savefig('Support_Vector_Regression.png')
plt.clf()

# Output Support Vector Regression Results w/ more data points
X_train_grid = np.arange(min(standardScaler_X.inverse_transform(X_train_scaled)), max(standardScaler_X.inverse_transform(X_train_scaled)), 0.1)
X_train_grid = X_train_grid.reshape((len(X_train_grid), 1))

plt.scatter(standardScaler_X.inverse_transform(X_train_scaled), standardScaler_Y.inverse_transform(Y_train_scaled), color = 'red')
plt.plot(X_train_grid, standardScaler_Y.inverse_transform(regressor.predict(standardScaler_X.transform(X_train_grid))), color = 'blue')
plt.title('Support Vector Regression Model w/ more data points')
plt.xlabel('Position Level')
plt.ylabel('Salary')
plt.savefig('Support_Vector_Regression_W_More_Data_Points.png')
plt.clf()