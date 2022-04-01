#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.x 
from data_manager import DataManager
from flight_search import FlightSearch

flight_search = FlightSearch()
data_manager = DataManager()
sheet_data = data_manager.get_prices()

#check if the sheet_data dictionary contains any values for the 'iatacode' field
if sheet_data[0]["iataCode"] == "":
    for row in sheet_data:
        row["iataCode"] = flight_search.get_iata(row["city"])
    print(f"sheet_data:\n {sheet_data}")

    data_manager.destination_data = sheet_data
    data_manager.update_code()


for dest in sheet_data:
    dest_iata = dest['iataCode']
    try:
        price = flight_search.search_flight(dest_iata)['data'][0]['price']
    except:
        price = 10000
    
    #print all flights that meet the lowest price
    if dest['lowestPrice'] > price:
        print("{}: ${}".format(dest['city'], price))
