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

# Random Forest Regressor
## Uses ensemble learning
## A Random Forest Regression model has better predictability compared to a Decision Tree Regression Model.  However, it has less interpretability.
### 1. Pick random K data points from Training Set.
### 2. Build the Decision Tree associated with these K points.
### 3. Choose the number N of trees to build and repeat #1 and #2
### 4.  For a new data point, make each one of your N trees predict the value for the point in question.  The new predicted output is the average across all the predicted N values.
## To evaluate the Random Forest regressor, compute the "Mean of Squared Residuals" (the mean of the squared errors).
## Can't apply Backward Elimination to Random Forest Regression models because there are no coefficients combined in a linear regression equation and therefore there are no p-values.

# Create and train the Random Forest Regression model
## Use 10 trees in the forest
from sklearn.ensemble import RandomForestRegressor
regressor = RandomForestRegressor(n_estimators = 10, random_state = 0)
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
plt.title('Random Forest Regression Model w/ more data points')
plt.xlabel('Position Level')
plt.ylabel('Salary')
plt.savefig('Random_Forest_Regression_W_More_Data_Points.png')
plt.clf()