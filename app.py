from flask import Flask, render_template, request, jsonify
import os

app = Flask(__name__)
app.config['STATIC_URL'] = '/static/'
app.config['STATIC_DIR'] = 'static/'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    question = request.form['question']
    api_response = send_request(question)
    if api_response:
        return render_template('result.html', result=api_response)
    else:
        return "Error: Unable to process your query."

def send_request(question):
    url = "https://api.openweathermap.org/data/2.5/weather?"
    params = {'q': question, 'appid': '<YOUR_OPENWEATHERMAP_APPID>'}
    try:
        response = requests.get(url, params=params).json()
        weather_info = response['weather']['description'].capitalize()
        temperature = round((response['main']['temp'] - 273.15), 1)
        location = response['name']
        return f"Weather in {location}: {weather_info}. Temperature: {temperature}°C."
    except Exception as e:
        print(str(e))
        return None

if __name__ == '__main__':
    app.run(debug=True)
