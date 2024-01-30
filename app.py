from flask import Flask, render_template, request, jsonify
import os
import requests

# Replace this with your OpenAI API key
OPENAI_API_KEY = "your_openai_api_key"

app = Flask(__name__)

# Define some sample messages and responses
sample_responses = {
    "hello": "Hi there! How has your day been?",
    "how was your day?": "Today was quite interesting. I learned a lot about AI.",
    "what did you learn today?": "I learned about natural language processing and how to create conversational bots."
}

def get_bot_response(context):
    message = context["message"]
    profile_picture_url = context["profile_picture_url"] or ""

    if message in sample_responses:
        response = sample_responses[message]
    else:
        # Make an API call to generate a response using the OpenAI API
        headers = {"Authorization": f"Bearer {OPENAI_API_KEY}", "Content-Type": "application/json"}
        data = {"prompt": message, "max_tokens": 100}
        response = requests.post("https://api.openai.com/v1/engines/davinci/generate", headers=headers, json=data).json()["choices"]["text"].strip()

    return response

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/chat", methods=["GET"])
def load_previous_conversation():
    conversation = []

    # Load the conversation from the local storage file
    try:
        with open("conversations.txt", "r") as f:
            conversations = f.read().splitlines()
            for c in conversations:
                conversation.append(c.split("\t"))
    except FileNotFoundError:
        pass

    return render_template("index.html", conversation=conversation[-1])

@app.route("/chat", methods=["POST"])
def chat():
    message = request.form["message"]
    profile_picture_url = request.form.get("profile_picture_url")

    # Save the current conversation to the local storage file
    with open("conversations.txt", "a") as f:
        f.write(f"{message}\t{profile_picture_url}")

    context = {"message": message, "profile_picture_url": profile_picture_url}
    response = get_bot_response(context)

    return jsonify({"response": response})

if __name__ == "__main__":
    app.run(debug=True)
