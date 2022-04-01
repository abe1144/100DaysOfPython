import requests

class DataManager:
    #This class is responsible for talking to the Google Sheet.
    def __init__(self):
        self.get_endpoint = "https://api.sheety.co/c4916d80c5f27f46953977929b42a114/flightDeals/prices"
        self.put_endpoint = "https://api.sheety.co/c4916d80c5f27f46953977929b42a114/flightDeals/prices/{}"
        self.destination = {}

    #method to get current prices from sheety
    def get_prices(self):
        response = requests.get(url=self.get_endpoint)
        self.destination = response.json()['prices']
        return self.destination

    def update_code(self):
        for city in self.destination_data:
            new_data = {
                "price": {
                    "iataCode": city["iataCode"]
                }
            }
            response = requests.put(
                url=self.put_endpoint.format(city['id']),
                json=new_data
            )
            print(response.text)

