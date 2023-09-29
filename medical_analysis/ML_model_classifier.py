import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import classification_report
from sklearn.tree import DecisionTreeClassifier
from sklearn.linear_model import LogisticRegression
import statsmodels.api as sm
from sklearn.feature_selection import RFE

# getting data:
df = pd.read_csv("medical_examination.csv")
pd.set_option('display.max_columns', None)
print(df.columns)
df.drop(['id', 'smoke', 'alco', 'sex'], axis=1, inplace=True)

# making new columns:
bmi = pd.Series([], dtype='float64')
print(len(df))
for i in range(len(df)):
    bmi[i] = 0
for i in range(len(df)):
    bmi[i] = df['weight'][i] / pow(df["height"][i] * 0.01, 2)

df.insert(6, 'BMI', bmi)
print(df.head(10))

# extracting input and output:
x = df.iloc[:, 0:9].values
y = df.iloc[:, 9].values

# making equal classes:
sns.countplot(x=y, palette='pastel')
plt.title('Classes', fontsize=12)
plt.show()
# they are almost equal

# splitting data into train, test :
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.20, random_state=21)

# feature normalization:
scaler = StandardScaler()
x_train = scaler.fit_transform(x_train)
x_test = scaler.transform(x_test)

# training data with classifier:
classifier = DecisionTreeClassifier(splitter='best', random_state=42)
classifier.fit(x_train, y_train)

# predictions:
y_pred = classifier.predict(x_test)
c_score = classifier.score(x_test, y_test)

# accuracy and overall score and confusion matrix:
score = np.mean(c_score)
print('Accuracy : %.3f ' % score)
print(classification_report(y_test, y_pred))
print(pd.crosstab(y_test, y_pred, rownames=['true classes'], colnames=['predicted classes']))
# features importance:
print(list(zip(df.columns[0:9], classifier.feature_importances_)))

# 2 class Logistic Regression :
df = pd.read_csv("medical_examination.csv")
pd.set_option('display.max_columns', None)

bmi = pd.Series([], dtype='float64')
print(len(df))
for i in range(len(df)):
    bmi[i] = 0
for i in range(len(df)):
    bmi[i] = df['weight'][i] / pow(df["height"][i] * 0.01, 2)

df.insert(11, 'BMI', bmi)
# extracting input and output:
x = df.iloc[:, 0:13].values
y = df.iloc[:, 13].values

# using RFE:
# logreg = LogisticRegression()
# rfe = RFE(logreg, n_features_to_select=13)
# rfe = rfe.fit(x, y)
# print(rfe.support_)
# print(rfe.ranking_)

# model:
logit_model = sm.Logit(y, x)
result = logit_model.fit()
print(result.summary2())
x = df.iloc[:, 1:13].values
# model fitting:
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=0)

# feature normalization:
scaler = StandardScaler()
x_train = scaler.fit_transform(x_train)
x_test = scaler.transform(x_test)

logreg = LogisticRegression()
logreg.fit(x_train, y_train)

# predictions and reports:
y_pred = logreg.predict(x_test)
print('Accuracy of Logistic Regression test: %.2f' % logreg.score(x_test, y_test))
print(pd.crosstab(y_test, y_pred, rownames=['true classes'], colnames=['predicted classes']))
print(classification_report(y_test, y_pred))

# CONCLUSIONS:
# ML model using Logistic Regression has better outcome with 71% accuracy
# then using Decision Tree Classifier (64% accuracy)
