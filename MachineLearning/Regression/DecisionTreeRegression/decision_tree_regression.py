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

# Decision Tree Regressor
## Two types: Classification Trees and Regression Trees (CART)
## Splits or 'terminal leaves' are created if they holistically reduce the standard deviation of the predictions.
## The Information Gain is the Standard Deviation Reduction.  The more the standard deviation decreases, the less the entropy and the more homogenous the child nodes become.
## No feature scaling is required because the splitting of data does not require it.
## Feature Selection is not possible because it is not linear.  However, Feature Extracting is possible using Dimensionality Reduction.

# Create and train the Decision Tree Regression model
from sklearn.tree import DecisionTreeRegressor
regressor = DecisionTreeRegressor(random_state = 0)
regressor.fit(X_train, Y_train)

# Predict salary for a 6.5 level position
Y_predict = regressor.predict([[6.5]])

# Output prediction salary for a 6.5 level position
print(f"Salary for a position 6.5 is = {Y_predict}")

# Output Decistion Tree Regression Results w/ more data points
X_train_grid = np.arange(min(X_train), max(X_train), 0.1)
X_train_grid = X_train_grid.reshape((len(X_train_grid), 1))

plt.scatter(X_train, Y_train, color = 'red')
plt.plot(X_train_grid, regressor.predict(X_train_grid), color = 'blue')
plt.title('Decision Tree Regression Model w/ more data points')
plt.xlabel('Position Level')
plt.ylabel('Salary')
plt.savefig('Decision_Tree_Regression_W_More_Data_Points.png')
plt.clf()