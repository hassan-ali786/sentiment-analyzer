# Sentiment Analyzer

Sentiment Analyzer is a web application built with Streamlit that predicts the sentiment of text data (positive, negative, or neutral) using Natural Language Processing (NLP) and Machine Learning.

This project is designed for real-world use cases such as analyzing product reviews, social media posts, and customer feedback.

---

## Live Demo:

[Click here to view the Live Demo](https://sentiment-analyzer-nsfp8ubwwjzjjjggfxi9by.streamlit.app/)

---

## Video Demo:

<video src="https://github.com/user-attachments/assets/919a8d18-2ebd-4cc3-aa9d-bcce5550cac2" width="100%" controls></video>

---


## Features

- Predicts sentiment (Positive / Negative / Neutral) from user input text  
- Fast and interactive Streamlit UI for real-time analysis  
- Clean and modular code structure  
- Trained on real-world datasets (IMDB and Twitter data)  
- Displays confidence score with predictions  
- Easily extendable for other NLP tasks  

---

## Project Structure

```bash
Sentiment_Analyzer/
├── data/
│   └── IMDB_Dataset.csv
├── models/
│   ├── model.pkl
│   └── vectorizer.pkl
├── src/
│   ├── preprocessing.py
│   ├── train_model.py
│   └── predict.py
├── notebooks/
│   └── EDA.ipynb
├── images/
│   └── homepage.png
├── app.py
├── requirements.txt
├── README.md
└── .gitignore
```
---

## Tech Stack

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white) ![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white) ![Scikit-Learn](https://img.shields.io/badge/Scikit-Learn-F7931E?style=for-the-badge&logo=scikit-learn&logoColor=white) ![NLTK](https://img.shields.io/badge/NLTK-85C1E9?style=for-the-badge) ![Pandas](https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white)

---

## Installation

### 1. Clone the repository


git clone https://github.com/hassan-ali786/sentiment-analyzer.git

cd sentiment-analyzer


### 2. Create virtual environment (recommended)


python -m venv venv


Activate environment:

Windows:

venv\Scripts\activate


Linux/macOS:

source venv/bin/activate


### 3. Install dependencies


pip install -r requirements.txt


### 4. Add dataset

Download IMDB dataset and place it in:


data/IMDB_Dataset.csv


---

## Usage

### Train the model (optional)


python src/train_model.py


### Run the application


streamlit run app.py


Open in browser:


http://localhost:8501


---

## How It Works

1. User enters text  
2. Text is preprocessed (cleaning, stopword removal)  
3. Converted into features using TF-IDF  
4. Model predicts sentiment  
5. Output shows sentiment and confidence score  

---

## Model Details

- Vectorizer: TF-IDF  
- Algorithm: Naive Bayes  
- Task: Text Classification  

---

## Dataset

- IMDB Movie Reviews Dataset  
- 50,000 labeled reviews (positive / negative)  

Optional:
- Twitter dataset for extended training  

---

## Example Input


This movie was absolutely amazing, I loved it!


Output:


Sentiment: Positive
Confidence: 92%


---

## Future Improvements

- Use advanced models like BERT  
- Add multi-language support  
- Create analytics dashboard  
- Deploy on Streamlit Cloud or Render  

---

## Use Cases

- Product review analysis  
- Social media sentiment tracking  
- Customer feedback analysis  
- NLP learning project  

---

## License

This project is open-source under the MIT License.

---

## Author

Hassan Ali  
Data Scientist & ML Engineer

---

##  Application Screenshot

![Home Page](https://raw.githubusercontent.com/hassan-ali786/sentiment-analyzer/main/images/homepage.png)

---
