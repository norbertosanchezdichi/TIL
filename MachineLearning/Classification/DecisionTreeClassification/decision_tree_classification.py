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
from sklearn.preprocessing import StandardScaler
standardScaler = StandardScaler()
X_train_scaled = standardScaler.fit_transform(X_train)
X_test_scaled = standardScaler.transform(X_test)

print(f"X_train_scaled = {X_train_scaled}")
print(f"X_test_scaled = {X_test_scaled}")
print()

# Decision Tree Classifier
## Splits the dataset into homogenous classes with the goal to obtain the minimum entropy in each terminal leaf.
### Uses reduction of standard deviation of the predictions.
### Building a decision tree is all about finding the attribute that returns the highest standard deviation reduction.
### The Information Gain is the reduction in standard deviation.
## Not useful on its own but are incorporated in other methods which makes the overall model powerful.
### Incorporated in Random Forest and used in Gradient Boosting.

# Create and train Decision Tree model
## Use entropy to measure the quality of the split.
from sklearn.tree import DecisionTreeClassifier
classifier = DecisionTreeClassifier(criterion = 'entropy', random_state = 0)
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
plt.title('Decision Tree (Training Set)')
plt.xlabel('Age')
plt.ylabel('Estimated Salary')
plt.legend()
plt.savefig('Decision_Tree_Training_Set_Results.png')
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
plt.title('Decision Tree (Test Set)')
plt.xlabel('Age')
plt.ylabel('Estimated Salary')
plt.legend()
plt.savefig('Decision_Tree_Test_Set_Results.png')
plt.clf()