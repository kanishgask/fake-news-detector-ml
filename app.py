from flask import Flask, request, render_template
import pickle

app = Flask(__name__)

# Load trained model
model = pickle.load(open("model.pkl", "rb"))
vectorizer = pickle.load(open("vectorizer.pkl", "rb"))

@app.route("/")
def home():
    return """
    <h2>Fake News Detector</h2>
    <form method="post" action="/predict">
        <input type="text" name="news" placeholder="Enter news headline" size="50">
        <button type="submit">Check News</button>
    </form>
    """

@app.route("/predict", methods=["POST"])
def predict():
    news = request.form["news"]

    news_vector = vectorizer.transform([news])
    prediction = model.predict(news_vector)

    if prediction[0] == 1:
        result = "This news is likely REAL"
    else:
        result = "This news is likely FAKE"

    return f"<h3>{result}</h3><br><a href='/'>Check another news</a>"

if __name__ == "__main__":
    app.run(debug=True)
