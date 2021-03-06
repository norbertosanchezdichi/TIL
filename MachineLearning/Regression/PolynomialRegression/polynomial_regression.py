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

# Create and train the Linear Regression model
from sklearn.linear_model import LinearRegression
linearRegressor = LinearRegression()
linearRegressor.fit(X_train, Y_train)

# Polynomial Regressor
## The Polynomial Regressor is linear on the coefficients because they are not raised to a power.
## However, the Polynomial Regressor is a non-linear function because the inputs are raised to a power.
## Feature Scaling is not required because the coefficients adjust to put everyting on the same scale.
## To evaluate the polynomial regressor, compute the "Mean of Squared Residuals" (the mean of the squared errors).
## Can't apply Backward Elimination to Polynomial Regression models because there are no coefficients combined in a linear regression equation and therefore there are no p-values.

# Create and train Polynomial Regression model
from sklearn.preprocessing import PolynomialFeatures
polynomialPreprocessor = PolynomialFeatures(degree = 4)
X_train_polynomial = polynomialPreprocessor.fit_transform(X_train)

linearRegressor_polynomial = LinearRegression()
linearRegressor_polynomial.fit(X_train_polynomial, Y)

# Output Linear Regression Results
plt.scatter(X_train, Y_train, color = 'red')
plt.plot(X_train, linearRegressor.predict(X_train), color = 'blue')
plt.title('Linear Regression Model')
plt.xlabel('Position Level')
plt.ylabel('Salary')
plt.savefig('Linear Regression.png')
plt.clf()

# Output Polynomial Regression Results
plt.scatter(X_train, Y_train, color = 'red')
plt.plot(X_train, linearRegressor_polynomial.predict(X_train_polynomial), color = 'blue')
plt.title('Polynomial Regression Model')
plt.xlabel('Position Level')
plt.ylabel('Salary')
plt.savefig('Polynomial_Regression.png')
plt.clf()

# Output Polynomial Regression Results w/ more data points
X_train_grid = np.arange(min(X_train), max(X_train), 0.1)
X_train_grid = X_train_grid.reshape((len(X_train_grid), 1))
X_train_polynomial_grid = polynomialPreprocessor.fit_transform(X_train_grid)

plt.scatter(X_train, Y_train, color = 'red')
plt.plot(X_train_grid, linearRegressor_polynomial.predict(X_train_polynomial_grid), color = 'blue')
plt.title('Polynomial Regression Model w/ More Data Points')
plt.xlabel('Position Level')
plt.ylabel('Salary')
plt.savefig('Polynomial_Regression_with_More_Data_Points.png')
plt.clf()

# Predict using Linear Regression
np.set_printoptions(precision = 2)
Y_linear_predict = linearRegressor.predict([[6.5]])

# Output prediction salary for a position 6 using linear regression.
print(f"Salary for a position 6 using linear regression is = {Y_linear_predict}\n")

# Predict using Polynomial Regression
Y_polynomial_predict = linearRegressor_polynomial.predict(polynomialPreprocessor.fit_transform([[6.5]]))

# Output prediction salary for a position 6 using linear regression.
print(f"Salary for a position 6 using polynomial regression is = {Y_polynomial_predict}\n")