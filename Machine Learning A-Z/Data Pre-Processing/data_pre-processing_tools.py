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

# Imputation: Replacing unknown independent values.
from sklearn.impute import SimpleImputer
imputer = SimpleImputer(missing_values = np.nan, strategy = 'mean')
imputer.fit(X[:, 1:3])
X[:, 1:3] = imputer.transform(X[:, 1:3])

print(f"X after imputation = {X}")
print()

# One-Hot Encoding: Encoding categorical data.
## Independent Variable
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder
columnTransformer = ColumnTransformer(transformers = [('encoder', OneHotEncoder(), [0])], remainder = 'passthrough')
X = np.array(columnTransformer.fit_transform(X))

print(f"X after one-hot encoding country column = {X}")

## Dependent Variable
from sklearn.preprocessing import LabelEncoder
labelEncoder = LabelEncoder()
Y = labelEncoder.fit_transform(Y)

print(f"Y after one-hot encoding = {Y}")
print()

# Splitting Dataset: Training Set and Test Set
from sklearn.model_selection import train_test_split
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size = 0.2, random_state = 1)

print(f"X_train = {X_train}")
print(f"X_test = {X_test}")
print(f"Y_train = {Y_train}")
print(f"Y_test = {Y_test}")
print()

# Feature Scaling (done after splitting to avoid information leakage.)
from sklearn.preprocessing import StandardScaler
standardScaler = StandardScaler()
X_train[:, 3:] = standardScaler.fit_transform(X_train[:, 3:])
X_test[:, 3:] = standardScaler.transform(X_test[:, 3:])

print(f"X_train after feature scaling = {X_train}")
print(f"X_test after feature scaling = {X_test}")
print()