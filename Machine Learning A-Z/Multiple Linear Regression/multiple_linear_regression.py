# Import libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Import dataset
dataset = pd.read_csv('50_Startups.csv')
X = dataset.iloc[:, :-1].values
Y = dataset.iloc[:, -1].values

print(f"X = {X}")
print(f"Y = {Y}")
print()

# One-Hot Encoding: Encoding categorical data where order is not of importance.
## Independent Variable
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder
columnTransformer = ColumnTransformer(transformers = [('encoder', OneHotEncoder(), [3])], remainder = 'passthrough')
X = np.array(columnTransformer.fit_transform(X))

print(f"X after one-hot encoding state column = {X}")
print()

# Split Dataset: Training Set and Test Set
from sklearn.model_selection import train_test_split
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size = 1/3, random_state = 0)

print(f"X_train = {X_train}")
print(f"X_test = {X_test}")
print(f"Y_train = {Y_train}")
print(f"Y_test = {Y_test}")
print()

# Train Multiple Regression model on Training Set
## LinearRegression takes care of the Dummy Variable Trap and employs Backward Elimination automatically to chose the best features that are statistically significant.
from sklearn.linear_model import LinearRegression
multipleRegressor = LinearRegression()
multipleRegressor.fit(X_train, Y_train)