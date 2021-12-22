#check if it will rain in the next 12 hours at 7am

import requests
from twilio.rest import Client
import os

key = os.environ.get("owm_api_key")

lat = 25.2
lon = 121.33

#leuven forecast
params = {"lat": lat, "lon": lon, "exclude":"current,minutely,daily", "appid":key}

url ="https://api.openweathermap.org/data/2.5/onecall"

response = requests.get(url, params=params)

response.raise_for_status()
weather_data = response.json()

#list of json: take first 12
hourly = weather_data['hourly'][:12]

rain = False
#id field indicates weather type < 5XX means rain
for dic in hourly:
    if dic['weather'][0]['id'] <= 599:
        rain=True

#Twilio

account_sid = os.environ.get("twilio_account_sid")
auth_token = os.environ.get("twilio_key")




if rain:
    client = Client(account_sid, auth_token)
    message = client.messages \
                .create(
                     body="It's going to rain today. Remember to bring an Umbrella.",
                     from_='+12695254318',
                     to=os.environ.get("cell_number")
                 )
    print(message.status)
