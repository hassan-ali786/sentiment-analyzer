import os
import pandas as pd
import pickle
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from src.preprocessing import clean_text  # fixed import

# Paths
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_PATH = os.path.join(BASE_DIR, 'data', 'IMDB Dataset.csv')
MODEL_PATH = os.path.join(BASE_DIR, 'models', 'model.pkl')
VECTORIZER_PATH = os.path.join(BASE_DIR, 'models', 'vectorizer.pkl')

# Load dataset
df = pd.read_csv(DATA_PATH)
df['review'] = df['review'].apply(clean_text)

# Split
X_train, X_test, y_train, y_test = train_test_split(df['review'], df['sentiment'], test_size=0.2, random_state=42)

# Vectorize
vectorizer = CountVectorizer()
X_train_vec = vectorizer.fit_transform(X_train)
X_test_vec = vectorizer.transform(X_test)

# Train model
model = MultinomialNB()
model.fit(X_train_vec, y_train)

# Save
os.makedirs(os.path.join(BASE_DIR, 'models'), exist_ok=True)
with open(MODEL_PATH, 'wb') as f:
    pickle.dump(model, f)
with open(VECTORIZER_PATH, 'wb') as f:
    pickle.dump(vectorizer, f)

print("Model trained and saved successfully.")