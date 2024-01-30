from flask import Flask, render_template, request, jsonify
import os
import openai

app = Flask(__name__)
app.config['STATIC_URL'] = '/static/'
app.config['STATIC_DIR'] = 'static/'

openai.api_key = "<your_openai_api_key>"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    message = request.form['message']
    response = get_bot_response(message)
    return jsonify({'response': response})

def get_bot_response(user_message):
    completion = openai.Completion.create(
        engine='davinci',
        prompt=user_message,
        max_tokens=100,
        n=1,
        stop=None,
        temperature=0.8
    )
    return completion.choices.text

if __name__ == '__main__':
    app.run(debug=True)
