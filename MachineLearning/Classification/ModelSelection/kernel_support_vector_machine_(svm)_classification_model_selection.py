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

# Kernel Support Vector Machine (SVM) Classifier
## Effective for data sets that are non-linearly separable by mapping to a higher dimension.
## The data set becomes separable by using a line, a hyperplane, or other structure with a dimension less than the mapped higher dimension.
## Mapping to a higher dimensional space can become computationally expensive.
# The Kernel Trick using the Gaussian Radial-Basis Function (RBF)
## Its a function of a vector and a landmark, which is the center of the peak of the function.
### Using Euler's number, the function is three-dimensional and uses σ to adjust the radius of the base of the peak.
## It is used to produce a decision boundary for a non-linearly separable dataset.
## By choosing the optimal place for the landmark in the non-linear dataset and by tuning σ, the dataset is easily separated into two categories.
## Multiple kernel functions can be used by adding them up such that multiple landmarks with a specific base radius are found to linearly separate the dataset in 3-D.  This allows to create a more complex decision boundary.
# Types of Kernel Functions
## Gaussian Radial-Basis Function (RBF) Kernel
## Sigmoid Kernel
## Polynomial Kernel
## mlkernels.readthedocs.io
# Non-Linear Support Vector Regression (SVR)
## Results in a non-linear separation between the two categories.
## For example, the intersection of three hyperplanes and the Gaussian RBF function is done in such a way that a non-linear solution projected to the 2-D space results in an accurate separation between the two categories.

# Create and train Kernel Support Vector Machine (SVM) model
## Use Gaussian Radial-Basis Function (RBF) kernel
from sklearn.svm import SVC
classifier = SVC(kernel = 'rbf', random_state = 0)
classifier.fit(X_train_scaled, Y_train)

# Predict using Kernel Support Vector Machine (SVM) model
Y_predict = classifier.predict(X_test_scaled)
print(f"[Y_predict Y_test] = {np.concatenate((Y_predict.reshape(len(Y_predict), 1), Y_test.reshape(len(Y_test), 1)), axis = 1)}")
print()

# Create Confusion Matrix
## Not the optimal method to evaluate the performance of the model - K-Fold Cross Validation is preferred and it involves using validation tests.
from sklearn.metrics import confusion_matrix
print(f"Confusion Matrix = {confusion_matrix(Y_test, Y_predict)}")
print()

# Generate Accuracy Score
from sklearn.metrics import accuracy_score
print(f"Accuracy Score = {accuracy_score(Y_test, Y_predict)}")