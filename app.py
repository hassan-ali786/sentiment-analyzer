import streamlit as st
from src.predict import predict_sentiment

st.title("IMDB Sentiment Analyzer")

review = st.text_area("Enter your movie review:")

if st.button("Analyze"):
    sentiment = predict_sentiment(review)
    st.write("Sentiment:", sentiment)