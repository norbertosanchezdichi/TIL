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
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size = 0.2, random_state = 0)

print(f"X_train = {X_train}")
print(f"X_test = {X_test}")
print(f"Y_train = {Y_train}")
print(f"Y_test = {Y_test}")
print()

# Train Multiple Regression model on Training Set
## Skikit-Learn library takes care of the Dummy Variable Trap and employs Backward Elimination automatically to chose the best features that are statistically significant.
### The Dummary Variable Trap was solved by eliminating the first One-Hot Encoding column because if the state is not one or the other, having a value 0 for the second and third column already gives this information.
from sklearn.linear_model import LinearRegression
regressor = LinearRegression()
regressor.fit(X_train, Y_train)

# Predict Test Set results
Y_predict = regressor.predict(X_test)

#Output Training and Test Set results
np.set_printoptions(precision = 2)
print(f"[Y_predict Y_test] = {np.concatenate((Y_predict.reshape(len(Y_predict), 1), Y_test.reshape(len(Y_test), 1)), axis = 1)}")