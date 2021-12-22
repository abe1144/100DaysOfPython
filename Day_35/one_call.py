#challenge:
#make a api call to one-call
#get hourly forecast for the next 48 hours

import requests

key = "7bb75c03c8b153132b870fda2c118d3b"

#leuven forecast for next 48
params = {"lat": 50.879845, "lon":4.700518,  "appid":key}

url ="https://api.openweathermap.org/data/2.5/onecall"

response = requests.get(url, params=params)

response.raise_for_status()
response.json()