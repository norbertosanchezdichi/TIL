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
## Not required for Logistic Regression, however, it improves training performance and final predictions.
## Not done for dependent variable Y because the Logistic Regression model used is binary.
from sklearn.preprocessing import StandardScaler
standardScaler = StandardScaler()
X_train_scaled = standardScaler.fit_transform(X_train)
X_test_scaled = standardScaler.transform(X_test)

print(f"X_train_scaled = {X_train_scaled}")
print(f"X_test_scaled = {X_test_scaled}")
print()

# Logistic Regression Classifier
## Using the Sigmoid Function with Euler's number, solving for the dependent variable 'Y' in terms of the probability allows to model the solution with a linear equation.
## The solution is in terms of probability using the natural log - hence why it is called Logistic Regression.
# Assumptions when using Logistic Regression
## 1. Binary Logistic Regreesion requires the dependent variable to be binary. Ordinal Logistic Regression requires the dependent variable to be ordinal.
## 2. Requires the observations to be independent of each other.
## 3. Requires little or no multicollinearity among the independent variables.
## 4. Requires that the independent variables are linearly related to the log odds.

# Create and train Logistic Regression model
from sklearn.linear_model import LogisticRegression
classifier = LogisticRegression(random_state = 0)
classifier.fit(X_train_scaled, Y_train)

# Predict using Logistic Regression
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
## Accuracy Paradox
### Do not rely just on the accuracy score to evaluate a model.
### If a model only generates True Negatives and False Negatives, or only False Positives and True Positives, the accuracy might increase!
from sklearn.metrics import accuracy_score
print(f"Accuracy Score = {accuracy_score(Y_test, Y_predict)}")

# Cumulative Accuracy Profile (CAP)
## Edit independent_variable_threshold definition depending on threshold of classifier output
Y_test_only_zeros_and_ones = np.all(Y_test == 0) or np.all(Y_test == 1)
independent_variable_threshold = 3
if not Y_test_only_zeros_and_ones:
	Y_test = (Y_test > independent_variable_threshold).astype(int)
	Y_predict = (Y_predict > independent_variable_threshold).astype(int)

Y_test_length = len(Y_test)
Y_test_one_count = np.sum(Y_test)
Y_test_zero_count = Y_test_length - Y_test_one_count


## Plot Perfect Model
plt.plot([0, Y_test_one_count, Y_test_length], [0, Y_test_one_count, Y_test_one_count], c = 'g', linewidth = 2, label = 'Perfect Model')

## Plot Cumulative Accuracy Profile (CAP) for Logistic Regression model
classifier_CAP = [y for _, y in sorted(zip(Y_predict, Y_test), reverse = True)]
plt.plot(np.arange(0, Y_test_length + 1), np.append([0], np.cumsum(classifier_CAP)), c = 'k', linewidth = 2, label = 'Logistic Regression Classifier')

## Plot Random Model
plt.plot([0, Y_test_length], [0, Y_test_one_count], c = 'r', linewidth = 2, label = 'Random Model')


plt.legend()
plt.title('Cumulative Accuracy Profile (CAP)')
plt.xlabel('# of Data Points in the Data Set')
plt.ylabel('# of Predictions')
plt.legend()
plt.savefig('Logistic_Regression_Classification_Cumulative_Accuracy_Profile_(CAP).png')
plt.clf()
