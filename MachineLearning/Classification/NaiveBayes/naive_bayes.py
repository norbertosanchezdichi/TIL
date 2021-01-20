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

# Naïve-Bayes Classifier
## A non-linear model with a probabilistic approach.
## Baye's Theorem
### 1. Calculate P(A|X) = P(X|A) * P(A) / P(X)
#### P(A) -> Prior Probability
##### Equal to probability of A given a total number of observations.
#### P(X) -> Marginal Likelihood
##### Select a radius around the obversation in question.
###### Radius is chosen in the same way as in KNN.
##### All obvervations that lie inside the radius are deemed similar to the original observation in question.
##### Equal to the total of these similar observations divided by the total number of observations.
#### P(X|A) -> Likelihood
##### Equal to the total number of the similar observations above divided by the number of observations in class A.
#### P(A|X) -> Posterior Probability
##### Calculate using Baye's Theorem
### 2. Calculate P(B|X) = P(X|B) * P(B) / P(X)
#### Use same procedure above
### 3. P(A|X) vs P(B|X)
#### Whichever is greater decides the class of the new observation in question.
## Why Naïve?
### Assumes the observations are independent.
### May still give good results eventhough the observations may be somewhat corrolated.
### Still used eventhough some correlation may exist between observations that define the classes.
## P(X) Shortcut
### The Marginal Likelihood does not chance whether Baye's Theorem is calculated for class A or B.
### Therefore, P(X|A) * P(A) = P(X|B) * P(B)

# Create and train Naïve-Bayes model
## Use Gaussian Radial-Basis Function (RBF) kernel
from sklearn.naive_bayes import GaussianNB
classifier = GaussianNB()
classifier.fit(X_train_scaled, Y_train)

# Predict if-purchase for 30 year old customer earning $87,000
Y_predict = classifier.predict(standardScaler.transform([[30, 87000]]))
Y_predict_probability = classifier.predict_proba(standardScaler.transform([[30, 87000]]))

# Output prediction salary for a position 6
print(f"Purchase possible from 30 year old earning $87,000? = {Y_predict}. What is the probability? = {Y_predict_probability}")
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
plt.title('Naïve-Bayes (Training Set)')
plt.xlabel('Age')
plt.ylabel('Estimated Salary')
plt.legend()
plt.savefig('Naïve_Bayes_Training_Set_Results.png')
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
plt.title('Naïve-Bayes (Test Set)')
plt.xlabel('Age')
plt.ylabel('Estimated Salary')
plt.legend()
plt.savefig('Naïve_Bayes_Test_Set_Results.png')
plt.clf()