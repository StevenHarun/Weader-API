from flask import Flask, render_template, request
import requests

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get_weather')
def get_weather():
    city = request.args.get('city')
    url = "https://weather-api99.p.rapidapi.com/weather"
    querystring = {"city": city}
    headers = {
        "X-RapidAPI-Key": "b496fb5920msh0e7c73b0c647039p1a4636jsnd01cfd7ae1da",
        "X-RapidAPI-Host": "weather-api99.p.rapidapi.com"
    }
    response = requests.get(url, headers=headers, params=querystring)
    return response.json()

if __name__ == '__main__':
    app.run(debug=True)
