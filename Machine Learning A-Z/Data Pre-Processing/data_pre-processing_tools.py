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
