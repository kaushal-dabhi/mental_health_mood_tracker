import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
import pickle

# Load the mood data
data = pd.read_csv('mood_data.csv')

# Convert categorical mood labels to numerical values
mood_mapping = {'Happy': 2, 'Neutral': 1, 'Sad': 0}
data['mood_label'] = data['mood'].map(mood_mapping)

# Features and target variable
X = data[['energy', 'sleep_hours', 'stress_level']]
y = data['mood_label']

# Split the data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train the model
clf = RandomForestClassifier()
clf.fit(X_train, y_train)

# Save the model
with open('mood_model.pkl', 'wb') as f:
    pickle.dump(clf, f)
