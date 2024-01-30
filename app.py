from flask import Flask, render_template, request, jsonify
import requests

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    question = request.form["question"]
    url = "https://ai-assistant-model.p.rapidapi.com"
    headers = {
        "X-RapidAPI-Key": "<your_api_key>",
        "Content-Type": "application/json",
    }
    payload = {"query": question}
    response = requests.post(url, headers=headers, json=payload)
    answer = response.json()["answer"]
    return f"Question: {question}\nAnswer: {answer}"

if __name__ == "__main__":
    app.run()
