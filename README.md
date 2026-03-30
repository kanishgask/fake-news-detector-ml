# Fake News Detector using Machine Learning

This project detects whether a news headline is **Real or Fake** using Machine Learning and NLP techniques.

## Features
- Detect fake news
- Text processing using TF-IDF
- Logistic Regression model
- Simple command-line interface

## Technologies Used
- Python
- Machine Learning
- NLP
- Scikit-learn

## Project Structure

fake-news-detector-ml
│
├── dataset.csv
├── train_model.py
├── predict_news.py
├── requirements.txt
└── README.md

## How to Run

1. Install dependencies

pip install -r requirements.txt

2. Train the model

python train_model.py

3. Predict news

python predict_news.py

## Example

Input:
Aliens landed in India yesterday

Output:
This news is likely FAKE
