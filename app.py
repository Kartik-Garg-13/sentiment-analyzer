from flask import Flask, request, jsonify, render_template
import joblib
import re
app = Flask(__name__)
from flask_cors import CORS
CORS(app)
model = joblib.load(r'C:\Users\Lenovo\OneDrive\Documents\codes\sentiment_analyzer\models\sentiment_model.pkl')
vectorizer = joblib.load(r'C:\Users\Lenovo\OneDrive\Documents\codes\sentiment_analyzer\models\tfidf_vectorizer.pkl')
@app.route('/')
def home():
    return render_template('index.html')
def clean_text(text):
    text = re.sub(r'<.*?>', ' ', text)
    text = text.lower()
    text = re.sub(r'[^a-zA-Z\s]', ' ', text)
    text = " ".join(text.split())
    return text
@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    review = data['text']
    cleaned = clean_text(review)
    vectorized = vectorizer.transform([cleaned])
    prediction = model.predict(vectorized)[0]
    confidence = model.predict_proba(vectorized).max()

    return jsonify({
        'label': prediction,
        'confidence': round(float(confidence), 2)*100
    })
if __name__ == '__main__':
    app.run(debug=True)