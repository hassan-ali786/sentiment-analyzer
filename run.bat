@echo off
cd %~dp0

echo Training model...
python -m src.train_model

echo Running Streamlit app...
streamlit run app.py
pause