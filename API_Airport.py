import requests

url = "https://world-airports-directory.p.rapidapi.com/v1/airports/Bandung"

querystring = {"page":"1","limit":"20","sortBy":"AirportName:asc"}

headers = {
	"X-RapidAPI-Key": "f31c0b58a8mshe237f178f97cd7ep1659c2jsn47ea950cb282",
	"X-RapidAPI-Host": "world-airports-directory.p.rapidapi.com"
}

response = requests.get(url, headers=headers, params=querystring)

print(response.json())