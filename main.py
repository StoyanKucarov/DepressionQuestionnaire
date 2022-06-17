import numpy as np  # Various math throughout the program
import pandas as pd  # Data conversion and processing
import seaborn as sb  # Confusion Matrix
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import confusion_matrix, precision_score, recall_score, accuracy_score
import GUI

df = pd.read_excel('Cleaned Data.xlsx')
# df.head()  # Extract and display the table

# (334, 31), Visible in PyCharm w/o using shape

dropped = ['I am currently employed at least part-time', 'I am on section 8 housing', 'I receive food stamps',
           'Annual income from social welfare programs', 'Household Income', 'Region', 'Device Type']
df.drop(columns=dropped, inplace=True)
# Doesn't even apply to BG / We're too young for them / Have values incompatible w/ the code

df['Annual income (including any social welfare programs) in BGN'] = df[
                                                                         'Annual income (including any social welfare programs) in USD'] * 1.87
# Again, we're not american
df.drop('Annual income (including any social welfare programs) in USD', axis=1, inplace=True)
# # Remove redundancy
# df.head(20)
# df.info()  # Null values present

for i in df:
    if i == 'Education' or i == 'Age' or i == 'Gender':
        df[i].dropna()
    else:
        df[i].fillna(df[i].median(), inplace=True)
# Null Value Purge

y = df['Depression']
df.drop('Depression', axis=1, inplace=True)
# The thing we're predicting

# df.info()
le_education = LabelEncoder()
le_age = LabelEncoder()
le_gender = LabelEncoder()

df['Education'] = le_education.fit_transform(df['Education'])
df['Age'] = le_age.fit_transform(df['Age'])
df['Gender'] = le_gender.fit_transform(df['Gender'])
# Standardizing preparation

scaler = StandardScaler()
df2 = scaler.fit_transform(df)
df2.shape
X = df.values
X.shape
# Standardizing

# Randomizing
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=24)
print(X_train.shape, y_train.shape)

# Training the model
lr = LogisticRegression(solver='liblinear')
lr.fit(X_train, y_train)
y_pred = lr.predict(X_test)
print(y_pred)
#
# # # Testing accuracy
# print(accuracy_score(y_test, y_pred))  # 0.86
# print(recall_score(y_test,y_pred)) # 0.64
# print(precision_score(y_test,y_pred)) # 0.69
# cf_matrix=confusion_matrix(y_test,y_pred)
# sb.heatmap(cf_matrix, annot=True)

# Testing RFC option
rf = RandomForestClassifier()
rf.fit(X_train, y_train)
y_pred2 = rf.predict(X_test)

print(accuracy_score(y_test,y_pred2)) # 0.86
print(recall_score(y_test,y_pred2)) # 0.71
print(precision_score(y_test,y_pred2)) # 0.66
cf_matrix2=confusion_matrix(y_test,y_pred2)
sb.heatmap(cf_matrix2, annot=True)

# We're testing for depression and RFC yields one less FP so we're running w/ that

# Test for someone who should be miserable
# inputs = np.array([1, 0, 0, 1, 0, 0, 1, 30, 1, 1, 1, 1, 42, 1, 0, 19, 1, 1, 1, 1, 3, 0, 1])
# inputs=inputs.reshape(1,-1)
# prediction=rf.predict(inputs) # 1
# print(prediction)

answers = []


def predict(list1):
    if len(list1) == 23:
        a = np.array(list1)
        a = a.reshape(1,-1)
        if rf.predict(a) == 0:
            GUI.QText.set('Clear of depression')
        else:
            GUI.QText.set('May suffer from depression, consult a medical professional')
