import streamlit as st
from src.predict import predict_sentiment
from src.xquik_source import search_xquik_posts

st.title("IMDB Sentiment Analyzer")

source = st.radio("Input source", ["Manual text", "Xquik search"], horizontal=True)

review = ""

if source == "Manual text":
    review = st.text_area("Enter your movie review:")
else:
    query = st.text_input("Search X posts:", value="python sentiment")
    limit = st.slider("Posts to load", min_value=1, max_value=20, value=5)

    if st.button("Load X posts"):
        try:
            st.session_state["xquik_posts"] = search_xquik_posts(query, limit)
        except RuntimeError as exc:
            st.warning(str(exc))
        except Exception:
            st.error("Unable to load X posts.")

    posts = st.session_state.get("xquik_posts", [])
    if posts:
        review = st.selectbox("Choose a post to analyze:", posts)

if st.button("Analyze"):
    if review.strip():
        sentiment = predict_sentiment(review)
        st.write("Sentiment:", sentiment)
    else:
        st.warning("Enter text or load an X post first.")
