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

# Split Dataset: Training Set and Test Set
from sklearn.model_selection import train_test_split
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size = 0.2, random_state = 0)

print(f"X_train = {X_train}")
print(f"X_test = {X_test}")
print(f"Y_train = {Y_train}")
print(f"Y_test = {Y_test}")
print()

# Create and train the Multiple Regression model
## Skikit-Learn library takes care of the Dummy Variable Trap and employs Backward Elimination automatically to chose the best features that are statistically significant.
### The Dummary Variable Trap was solved by eliminating the first One-Hot Encoding column because if the state is not one or the other, having a value 0 for the second and third column already gives this information.
from sklearn.linear_model import LinearRegression
regressor = LinearRegression()
regressor.fit(X_train, Y_train)

# Predict Test Set results
Y_predict = regressor.predict(X_test)

# Output Training and Test Set results
np.set_printoptions(precision = 2)
print(f"[Y_predict Y_test] = {np.concatenate((Y_predict.reshape(len(Y_predict), 1), Y_test.reshape(len(Y_test), 1)), axis = 1)}")
print()

# Print multiple linear regressor coefficient and intercept.
print(f"Coefficients = {regressor.coef_}")
print(f"Intercept = {regressor.intercept_}")
print()

# Evaluate Model Performance
from sklearn.metrics import r2_score
print(f"R2 Score = {r2_score(Y_test, Y_predict)}")

print(f"Adusted R2 Score = {1 - (1 - r2_score(Y_test, Y_predict)) * ((len(X_test) - 1) / (len(X_test) - len(X_test[0]) - 1))}")
