import requests
import os
import datetime as dt
from pprint import pprint

class FlightSearch:
    #This class is responsible for talking to the Flight Search API.
    def __init__(self):
        self.location_endpoint = "https://tequila-api.kiwi.com/locations/query"
        self.search_enpoint = "https://tequila-api.kiwi.com/v2/search"
        self.api_key = os.environ.get('kiwiapi')
        self.origin="BRU"
        self.headers = {
            "apikey":self.api_key
        }
        self.departure_start_date = dt.datetime.today().strftime('%d/%m/%Y')
        self.departure_end_date = (dt.datetime.today() + dt.timedelta(days=180)).strftime('%d/%m/%Y')

    def get_iata(self, city):
        query = {
            "term": city,
            "location_types": "city"
        } 
        response = requests.get(url=self.location_endpoint, headers=self.headers, params=query)
        #take the first location if there are multiple
        results = response.json()['locations'][0]['code']
        return results

    def search_flight(self, iataDest):
        query = {
            "fly_from": self.origin,
            "fly_to":iataDest,
            "date_from":self.departure_start_date,
            "date_to":self.departure_end_date,
            "nights_in_dst_from":3,
            "nights_in_dst_to": 7,
            "max_stopovers":0

        }
        response = requests.get(url=self.search_enpoint, headers=self.headers, params=query)
        return response.json()

