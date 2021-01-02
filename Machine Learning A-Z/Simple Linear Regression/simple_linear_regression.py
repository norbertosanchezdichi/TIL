# Import libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Import dataset
dataset = pd.read_csv('Salary_Data.csv')
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

# Train Simple Linear Regression model on Training Set
from sklearn.linear_model import  LinearRegression
linearRegressor = LinearRegression()
linearRegressor.fit(X_train, Y_train)

# Predict Test Set results
Y_predict = linearRegressor.predict(X_test)

# Output Training Set results
plt.scatter(X_train, Y_train, color = 'red')
plt.plot(X_train, linearRegressor.predict(X_train), color = 'blue')
plt.title('Salary v. Years of Experience (Training Set)')
plt.xlabel('Years of Experience (years)')
plt.ylabel('Salary ($)')
plt.savefig('Salary v. Years of Experience (Training Set).png')
plt.clf()

# Output Test Set results
plt.scatter(X_test, Y_test, color = 'red')
plt.plot(X_test, Y_predict, color = 'blue')
plt.title('Salary v. Years of Experience (Test Set)')
plt.xlabel('Years of Experience (years)')
plt.ylabel('Salary ($)')
plt.savefig('Salary v. Years of Experience (Test Set).png')
plt.clf()