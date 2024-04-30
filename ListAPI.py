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

import requests

url = "https://world-airports-directory.p.rapidapi.com/v1/airports/Jakarta"

querystring = {"page":"1","limit":"20","sortBy":"AirportName:asc"}

headers = {
	"X-RapidAPI-Key": "f31c0b58a8mshe237f178f97cd7ep1659c2jsn47ea950cb282",
	"X-RapidAPI-Host": "world-airports-directory.p.rapidapi.com"
}

response = requests.get(url, headers=headers, params=querystring)

print(response.json())