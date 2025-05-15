import pandas as pd
import numpy as np
import pickle
import os
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestClassifier
from sklearn.utils import resample
from sklearn.metrics import classification_report, accuracy_score
# Load the dataset
df = pd.read_csv("plants.csv", encoding="cp1252")
# Encode categorical variables
label_encoders = {}
df_encoded = df.copy()
for col in df_encoded.columns:
    if df_encoded[col].dtype == "object":
        le = LabelEncoder()
        df_encoded[col] = le.fit_transform(df_encoded[col])
        label_encoders[col] = le
# Balance the growth classes
growth_col = df_encoded["Growth"]
moderate_class = label_encoders["Growth"].transform(["moderate"])[0]
fast_class = label_encoders["Growth"].transform(["fast"])[0]
slow_class = label_encoders["Growth"].transform(["slow"])[0]
df_moderate = df_encoded[df_encoded["Growth"] == moderate_class]
df_fast = df_encoded[df_encoded["Growth"] == fast_class]
df_slow = df_encoded[df_encoded["Growth"] == slow_class]
df_fast_upsampled = resample(df_fast, replace=True, n_samples=len(df_moderate), random_state=42)
df_slow_upsampled = resample(df_slow, replace=True, n_samples=len(df_moderate), random_state=42)
df_balanced = pd.concat([df_moderate, df_fast_upsampled, df_slow_upsampled])
# Define features and labels
X = df_balanced.drop(columns=["Plant Name", "Growth"])
y = df_balanced["Growth"]
feature_columns = X.columns.tolist()
# Train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
# Train RandomForest model
model = RandomForestClassifier(n_estimators=100, class_weight="balanced", random_state=42)
model.fit(X_train, y_train)
# Evaluate model;
y_pred = model.predict(X_test)
print("Accuracy:", round(accuracy_score(y_test, y_pred) * 100, 2), "%")
print("\nClassification Report:\n", classification_report(y_test, y_pred, target_names=label_encoders["Growth"].classes_))
# Save model
os.makedirs("model", exist_ok=True)
with open("model/model.pkl", "wb") as f:
    pickle.dump((model, label_encoders, feature_columns), f)
print("Model and encoders saved to model/model.pkl")
 

 
