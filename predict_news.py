import pickle

# Load model and vectorizer
model = pickle.load(open("model.pkl", "rb"))
vectorizer = pickle.load(open("vectorizer.pkl", "rb"))

# Input news
news = input("Enter news headline: ")

# Convert to vector
news_vector = vectorizer.transform([news])

# Predict
prediction = model.predict(news_vector)

if prediction[0] == 1:
    print("This news is likely REAL")
else:
    print("This news is likely FAKE")
