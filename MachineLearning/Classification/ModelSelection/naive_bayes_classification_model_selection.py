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

# Naïve-Bayes Classifier
## A non-linear model with a probabilistic approach.
## Helps rank predictions by their probability.
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

# Predict using Naïve-Bayes model
Y_predict = classifier.predict(X_test_scaled)
print(f"[Y_predict Y_test] = {np.concatenate((Y_predict.reshape(len(Y_predict), 1), Y_test.reshape(len(Y_test), 1)), axis = 1)}")
print()

# Create Confusion Matrix
## Not the optimal method to evaluate the performance of the model - K-Fold Cross Validation is preferred and it involves using validation tests.
from sklearn.metrics import confusion_matrix
print(f"Confusion Matrix = {confusion_matrix(Y_test, Y_predict)}")
print()

# Generate Accuracy Score
## Accuracy Paradox
### Do not rely just on the accuracy score to evaluate a model.
### If a model only generates True Negatives and False Negatives, or only False Positives and True Positives, the accuracy might increase!
from sklearn.metrics import accuracy_score
print(f"Accuracy Score = {accuracy_score(Y_test, Y_predict)}")
print()

# Cumulative Accuracy Profile (CAP)
## Accuracy Ratio = Area under Perfect Model / Aread under Classifier CAP
### If Accuracy Ratio > 90%, may be overfitting or may have forward-looking variables.
### If Accuracy Ratio < 70%, consider another model. 
## Edit independent_variable_threshold definition depending on threshold of classifier output
Y_train_only_zeros_and_ones = True
for y in Y_train:
    if not ((y == 0) or (y == 1)):
        Y_train_only_zeros_and_ones = False
        break

independent_variable_threshold = 3
if not Y_train_only_zeros_and_ones:
    Y_test = (Y_test > independent_variable_threshold).astype(int)
    Y_predict = (Y_predict > independent_variable_threshold).astype(int)

Y_test_length = len(Y_test)
Y_test_one_count = np.sum(Y_test)
Y_test_zero_count = Y_test_length - Y_test_one_count

## Plot Perfect Model
plt.plot([0, Y_test_one_count, Y_test_length], [0, Y_test_one_count, Y_test_one_count], c = 'g', linewidth = 2, label = 'Perfect Model')

## Plot Cumulative Accuracy Profile (CAP) for classifier
classifier_CAP = [y for _, y in sorted(zip(Y_predict, Y_test), reverse = True)]
plt.plot(np.arange(0, Y_test_length + 1), np.append([0], np.cumsum(classifier_CAP)), c = 'k', linewidth = 2, label = 'Naïve-Bayes Classifier')

## Plot Random Model
plt.plot([0, Y_test_length], [0, Y_test_one_count], c = 'r', linewidth = 2, label = 'Random Model')

## Area under Random Model
random_model_area = np.trapz([0, Y_test_one_count], [0, Y_test_length])

## Area under classifier CAP
classifier_CAP_area = np.trapz(np.append([0], np.cumsum(classifier_CAP)), np.arange(0, Y_test_length + 1)) - random_model_area

## Area under Perfect Model
perfect_model_area = np.trapz([0, Y_test_one_count, Y_test_one_count], [0, Y_test_one_count, Y_test_length]) - random_model_area

## Accuracy Ratio
accuracy_ratio = classifier_CAP_area / perfect_model_area
print(f"Accuracy Ratio = {accuracy_ratio}")

plt.legend()
plt.title(f"Cumulative Accuracy Profile (CAP), AR = {round(accuracy_ratio, 3)}")
plt.xlabel('# of Data Points in Y_test')
plt.ylabel('# of True Positive Predictions')
plt.legend()
plt.savefig('Naive_Bayes_Classification_Cumulative_Accuracy_Profile_(CAP).png')
plt.clf()
