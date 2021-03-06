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
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size = 1/3, random_state = 0)

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
### The P-Value only applies to linear models.

# Create and train Simple Linear Regression model
from sklearn.linear_model import LinearRegression
regressor = LinearRegression()
regressor.fit(X_train, Y_train)

# Predict Test Set results
Y_predict = regressor.predict(X_test)

# Output Training Set results
plt.scatter(X_train, Y_train, color = 'red')
plt.plot(X_train, regressor.predict(X_train), color = 'blue')
plt.title('Salary v. Years of Experience (Training Set)')
plt.xlabel('Years of Experience (years)')
plt.ylabel('Salary ($)')
plt.savefig('Salary_v_Years_of_Experience_(Training_Set).png')
plt.clf()

# Output Test Set results
plt.scatter(X_test, Y_test, color = 'red')
plt.plot(X_test, Y_predict, color = 'blue')
plt.title('Salary v. Years of Experience (Test Set)')
plt.xlabel('Years of Experience (years)')
plt.ylabel('Salary ($)')
plt.savefig('Salary_v_Years_of_Experience_(Test_Set).png')
plt.clf()

# Predict salary with 12 years of experience
print(f"Salary w/ 12 YoE = {regressor.predict([[12]])}\n")

# Print simple linear regressor coefficient and intercept
print(f"Coefficient = {regressor.coef_}")
print(f"Intercept = {regressor.intercept_}")