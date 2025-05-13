import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import classification_report

# Load data
df = pd.read_csv('../data/sample_trip_data.csv')

# Feature engineering
df['frequent_user'] = df['ride_count'] > 5
X = df[['ride_count', 'avg_rating', 'cancellation_count']]
y = df['churned']

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Logistic Regression
lr = LogisticRegression()
lr.fit(X_train, y_train)
print("Logistic Regression:")
print(classification_report(y_test, lr.predict(X_test)))

# Decision Tree
dt = DecisionTreeClassifier()
dt.fit(X_train, y_train)
print("Decision Tree:")
print(classification_report(y_test, dt.predict(X_test)))
