from flask import Flask, render_template, request, jsonify
import requests

app = Flask(__name__)

# Fungsi untuk mengambil data cuaca dari API weather
def get_weather_data(city):
    url = "https://weather-api138.p.rapidapi.com/weather"
    querystring = {"city_name": city}
    headers = {
        "X-RapidAPI-Key": "b496fb5920msh0e7c73b0c647039p1a4636jsnd01cfd7ae1da",
        "X-RapidAPI-Host": "weather-api138.p.rapidapi.com"
    }
    response = requests.get(url, headers=headers, params=querystring)
    return response.json()

# Fungsi untuk mengambil data bandara dari API world-airports-directory
def get_airport_data(city):
    url = "https://world-airports-directory.p.rapidapi.com/v1/airports/" + city
    querystring = {"page": "1", "limit": "20", "sortBy": "AirportName:asc"}
    headers = {
        "X-RapidAPI-Key": "f31c0b58a8mshe237f178f97cd7ep1659c2jsn47ea950cb282",
	    "X-RapidAPI-Host": "world-airports-directory.p.rapidapi.com"
    }
    response = requests.get(url, headers=headers, params=querystring)
    airport_data = response.json()['results'] if 'results' in response.json() else []
    return airport_data

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get_data')
def get_data():
    city = request.args.get('city')

    # Ambil data cuaca dan bandara menggunakan fungsi yang sudah dibuat
    weather_data = get_weather_data(city)
    airport_data = get_airport_data(city)

    # Masukkan data cuaca dan bandara ke dalam template HTML
    return jsonify({'city':city, 'weather':weather_data, 'airport':airport_data})

if __name__ == '__main__':
    app.run(debug=True) 