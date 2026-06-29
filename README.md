# Sentiment Analyzer

A web application that takes a movie review and predicts 
whether it is positive or negative.

## What it does
Type any movie review into the text box, click Analyze, 
and the app tells you the sentiment along with a confidence 
percentage.

## Tech Stack
- Python
- Pandas (data cleaning)
- Scikit-learn (TF-IDF, Logistic Regression)
- Flask (REST API)
- HTML, CSS, JavaScript (frontend)

## Model Performance
- Accuracy: 90%
- Dataset: IMDB 50,000 movie reviews

## How to run locally

1. Clone the repo
   git clone https://github.com/yourusername/sentiment-analyzer

2. Install dependencies
   pip install pandas scikit-learn flask flask-cors joblib

3. Train the model
   Run explore.ipynb in Jupyter notebook

4. Start the server
   python app.py

5. Open browser
   http://127.0.0.1:5000

## What I learned
- How TF-IDF converts text into numbers that a 
  machine learning model can learn from
- How to build and expose a trained ML model 
  as a REST API using Flask
- How to connect a JavaScript frontend to a 
  Flask backend using fetch()

## Screenshots
![alt text](<Screenshot 2026-06-30 023107.png>)
![alt text](<Screenshot 2026-06-30 023223.png>)