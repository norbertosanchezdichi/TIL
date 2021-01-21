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
## Use the mean to replace unknown independent values only if a few are missing.
## Other imputation strategies: median, most frequency, and prediction imputation.
### The Prediction Imputation strategy involves using a ML model to predict the unknown values.
#### 1. Set the feature column with missing values as the dependent variable.
#### 2. Set the other columns that don't have unknown values as your independent variable.
#### 3. Split the dataset into a Training and Test set.  The Training set has observations where the independent variable has no unknown values while the Test set has all the observations with unknown values.
#### 4. Then perform predictions to replace the uknown values.
from sklearn.impute import SimpleImputer
imputer = SimpleImputer(missing_values = np.nan, strategy = 'mean')
imputer.fit(X[:, 1:3])
X[:, 1:3] = imputer.transform(X[:, 1:3])

print(f"X after imputation = {X}")
print()

# One-Hot Encoding: Encoding categorical data where order is not of importance.
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

# Split Dataset: Training Set and Test Set
## The Training Set is a subset of the data on which the model will learn how to predict the dependent variable.
## The Test Set is the complimentary subset from the training set on which the odel is evaluated on.
## The sets are split based on the distribution of the values of the dependent variables.
from sklearn.model_selection import train_test_split
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size = 0.2, random_state = 1)

print(f"X_train = {X_train}")
print(f"X_test = {X_test}")
print(f"Y_train = {Y_train}")
print(f"Y_test = {Y_test}")
print()

# Feature Scaling 
## Done after splitting to avoid information leakage.
## Leakage is the use of information in the model training process which would not be expected to be available at prediction time.
### Causes the predictive scores to overestimate the model's utility when run in a production environment.
## Feature Scaling is done to optimize the accuracy of model predictions.
### It should be avoided if the goal is to keep the most interpration as possible about the model.
### Use Normalization when the data is normally distributed.
### Use Standardization when the data is not normally distributed.
from sklearn.preprocessing import StandardScaler
standardScaler = StandardScaler()
X_train[:, 3:] = standardScaler.fit_transform(X_train[:, 3:])
X_test[:, 3:] = standardScaler.transform(X_test[:, 3:])

print(f"X_train after feature scaling = {X_train}")
print(f"X_test after feature scaling = {X_test}")
print()