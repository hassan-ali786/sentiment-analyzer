import os
import pickle
from src.preprocessing import clean_text  # fixed import

# Paths
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MODEL_PATH = os.path.join(BASE_DIR, 'models', 'model.pkl')
VECTORIZER_PATH = os.path.join(BASE_DIR, 'models', 'vectorizer.pkl')

# Load model & vectorizer
with open(MODEL_PATH, 'rb') as f:
    model = pickle.load(f)
with open(VECTORIZER_PATH, 'rb') as f:
    vectorizer = pickle.load(f)

def predict_sentiment(text):
    text = clean_text(text)
    vec = vectorizer.transform([text])
    pred = model.predict(vec)
    return pred[0]

if __name__ == "__main__":
    while True:
        review = input("Enter review (or 'exit' to quit): ")
        if review.lower() == 'exit':
            break
        print("Sentiment:", predict_sentiment(review))