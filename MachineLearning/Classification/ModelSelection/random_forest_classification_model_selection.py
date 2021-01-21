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
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size = 0.25, random_state = 0)

print(f"X_train = {X_train}")
print(f"X_test = {X_test}")
print(f"Y_train = {Y_train}")
print(f"Y_test = {Y_test}")
print()

# Feature Scaling (done after splitting to avoid information leakage.)
from sklearn.preprocessing import StandardScaler
standardScaler = StandardScaler()
X_train_scaled = standardScaler.fit_transform(X_train)
X_test_scaled = standardScaler.transform(X_test)

print(f"X_train_scaled = {X_train_scaled}")
print(f"X_test_scaled = {X_test_scaled}")
print()

# Random Forest Classifier
## Uses Ensemble Learning - leverages a number of Decision Tree models.
### 1. Pick at random K data points from the Training Set.
### 2. Build the Decision Tree associated to these K data points.
### 3. Choose the number N of trees to build and repeat steps 1 and 2.
### 4. For a new data point, make each one of your N trees predict the category.  Assign the new data point to the category that wins the majority vote.
## Gives better predictive power than Decision Trees.
## It does not give the same intrepability as a Decision Tree.  You cannot do the same with a Random Forest.
## To find the optimal number of Decision Trees, use k-Fold Cross Validation and Grid Search.

# Create and train Random Forest model
## Use 10 trees in the forest
## Use entropy to measure the quality of the split.
from sklearn.ensemble import RandomForestClassifier
classifier = RandomForestClassifier(n_estimators = 100, criterion = 'entropy', random_state = 0)
classifier.fit(X_train_scaled, Y_train)

# Predict using Random Forest model
Y_predict = classifier.predict(X_test_scaled)
print(f"[Y_predict Y_test] = {np.concatenate((Y_predict.reshape(len(Y_predict), 1), Y_test.reshape(len(Y_test), 1)), axis = 1)}")
print()

# Compute prediction probability
Y_predict_probability = classifier.predict_proba(standardScaler.transform(X_train_scaled))
print(f"Y_predict_probability = {Y_predict_probability}")
print()

# Create Confusion Matrix
## Not the optimal method to evaluate the performance of the model - K-Fold Cross Validation is preferred and it involves using validation tests.
from sklearn.metrics import confusion_matrix
print(f"Confusion Matrix = {confusion_matrix(Y_test, Y_predict)}")
print()

# Generate Accuracy Score
from sklearn.metrics import accuracy_score
print(f"Accuracy Score = {accuracy_score(Y_test, Y_predict)}")
