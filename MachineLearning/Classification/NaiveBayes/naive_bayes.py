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
## Baye's Theorem
### 1. Calculate P(A|X) = P(X|A) * P(A) / P(X)
#### P(A) -> Prior Probability
##### Equal to probability of A given a total number of observations.
#### P(X) -> Marginal Likelihood
##### Select a radius around the obversation in question.
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
