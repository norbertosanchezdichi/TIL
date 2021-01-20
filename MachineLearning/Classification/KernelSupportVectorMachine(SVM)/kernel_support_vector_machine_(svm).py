# Import libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Import dataset
dataset = pd.read_csv('Social_Network_Ads.csv')
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
## Not required for Logistic Regression, however, it improves training performance and final predictions.
## Not done for dependent variable Y because the Logistic Regression model used is binary.
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

# Predict if-purchase for 30 year old customer earning $87,000
Y_predict = classifier.predict(standardScaler.transform([[30, 87000]]))

# Output prediction salary for a position 6
print(f"Purchase possible from 30 year old earning $87,000? = {Y_predict}.")
print()

# Predicting using Logistic Regression
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

# Output Training Set Results
from matplotlib.colors import ListedColormap
X_set, Y_set = standardScaler.inverse_transform(X_train_scaled), Y_train
X1, X2 = np.meshgrid(np.arange(start = X_set[:, 0].min() - 10, stop = X_set[:, 0].max() + 10, step = 1),
                     np.arange(start = X_set[:, 1].min() - 1000, stop = X_set[:, 1].max() + 1000, step = 1))
plt.contourf(X1, X2, classifier.predict(standardScaler.transform(np.array([X1.ravel(), X2.ravel()]).T)).reshape(X1.shape),
             alpha = 0.75, cmap = ListedColormap(('red', 'green')))
plt.xlim(X1.min(), X1.max())
plt.ylim(X2.min(), X2.max())
for i, j in enumerate(np.unique(Y_train)):
    plt.scatter(X_set[Y_train == j, 0], X_set[Y_train == j, 1], c = ListedColormap(('red', 'green'))(i), label = j)
plt.title('Kernel Support Vector Machine (SVM) (Training Set)')
plt.xlabel('Age')
plt.ylabel('Estimated Salary')
plt.legend()
plt.savefig('Kernel_Support_Vector_Machine_Training_Set_Results.png')
plt.clf()

# Output Test Set Results
from matplotlib.colors import ListedColormap
X_set, Y_set = standardScaler.inverse_transform(X_test_scaled), Y_test
X1, X2 = np.meshgrid(np.arange(start = X_set[:, 0].min() - 10, stop = X_set[:, 0].max() + 10, step = 1),
                     np.arange(start = X_set[:, 1].min() - 1000, stop = X_set[:, 1].max() + 1000, step = 1))
plt.contourf(X1, X2, classifier.predict(standardScaler.transform(np.array([X1.ravel(), X2.ravel()]).T)).reshape(X1.shape),
             alpha = 0.75, cmap = ListedColormap(('red', 'green')))
plt.xlim(X1.min(), X1.max())
plt.ylim(X2.min(), X2.max())
for i, j in enumerate(np.unique(Y_test)):
    plt.scatter(X_set[Y_test == j, 0], X_set[Y_test == j, 1], c = ListedColormap(('red', 'green'))(i), label = j)
plt.title('Kernel Support Vector Machine (SVM) (Test Set)')
plt.xlabel('Age')
plt.ylabel('Estimated Salary')
plt.legend()
plt.savefig('Kernel_Support_Vector_Machine_Test_Set_Results.png')
plt.clf()