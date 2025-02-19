from sklearn.model_selection import train_test_split
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.multioutput import MultiOutputClassifier
from sklearn.metrics import accuracy_score, confusion_matrix

df = pd.read_csv("Super6.csv")
print(df.shape)
X = df.iloc[:,5:45]
y = df.iloc[:, 63]
print(X)
print(y)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3,random_state=42)

scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# Step 2: Create the base model (Logistic Regression in this case)
base_model = LogisticRegression(max_iter=200)

base_model.fit(X_train, y_train)

y_pred = base_model.predict(X_test)

accuracy = accuracy_score(y_test, y_pred)
conf_matrix = confusion_matrix(y_test.values, y_pred)
print(accuracy)
print(conf_matrix)

print(base_model.coef_)
print(base_model.intercept_)