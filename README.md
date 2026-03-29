# Sentiment Analyzer 

**Sentiment Analyzer** is a web application built with **Streamlit** that predicts the sentiment of text data—positive, negative, or neutral—using **Natural Language Processing (NLP)** and **Machine Learning**. This project is designed for real-world applications like analyzing product reviews, social media posts, and customer feedback.

---

## **Features**

- Predicts sentiment (Positive / Negative / Neutral) from user input text.
- Fast and interactive **Streamlit UI** for real-time analysis.
- Clean and modular code structure for easy scalability.
- Trained on **real-world datasets** (IMDB movie reviews and Twitter data).
- Confidence score displayed with each prediction.
- Easily extendable to other NLP tasks like review classification or text analytics.

---

## **Folder Structure**

```text
Sentiment_Analyzer/
│
├── data/                  # Raw datasets (CSV files)
│   └── imdb_reviews.csv
├── models/                # Trained ML models and vectorizers
│   ├── model.pkl
│   └── vectorizer.pkl
├── src/                   # Python scripts
│   ├── preprocessing.py
│   ├── model.py           # Training script
│   └── predict.py         # Prediction functions
├── app.py                 # Streamlit application
└── requirements.txt
Installation

Clone the repository:

git clone https://github.com/yourusername/sentiment-analyzer.git
cd sentiment-analyzer

Create a virtual environment (recommended):

python -m venv venv
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate     # Windows

Install dependencies:

pip install -r requirements.txt

Download the IMDB dataset and place it in data/imdb_reviews.csv.

Usage

Train the model (optional if models/ already has trained models):

python src/model.py

Run the Streamlit app:

streamlit run app.py

Enter your text in the input box and click "Analyze Sentiment".

The app will display the predicted sentiment and confidence score.

Technologies Used

Python 3.10+

Streamlit – Frontend and web app framework

scikit-learn – Machine learning algorithms

NLTK – Text preprocessing and stopword removal

Pandas – Data manipulation

TF-IDF Vectorizer – Feature extraction from text

Naive Bayes Classifier – Sentiment classification

Dataset

IMDB Movie Reviews Dataset – 50,000 movie reviews labeled as positive or negative.
Kaggle Link

Optional: You can extend this project using Twitter data or your own text dataset.

Future Improvements

Use advanced models like BERT for better accuracy.

Multi-language support for reviews in different languages.

Add a dashboard with sentiment distribution charts.

Deploy on Streamlit Cloud or Heroku for public access.

License

This project is open-source and available under the MIT License.
