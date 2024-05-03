import requests

url = "https://weather-api138.p.rapidapi.com/weather"

querystring = {"city_name":"Cimahi"}

headers = {
	"X-RapidAPI-Key": "b496fb5920msh0e7c73b0c647039p1a4636jsnd01cfd7ae1da",
	"X-RapidAPI-Host": "weather-api138.p.rapidapi.com"
}

response = requests.get(url, headers=headers, params=querystring)

print(response.json())


# -----------------

