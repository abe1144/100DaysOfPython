import requests
import os
import datetime as dt
from requests.api import delete

from requests.models import Response

pixela_endpoint = "https://pixe.la/v1/users"

#signing up for an account
user_params = {
    "token": os.environ.get("pixela_token"),
    "username": os.environ.get("pixela_user"),
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

#Creating a Graph
graph_endpoint = "{}/{}/graphs".format(pixela_endpoint, os.environ.get("pixela_user"))

graph_config = {"id":"graph1", "name":"Push Up Graph", "unit": "reps","type":"int", "color":"shibafu"}
headers = {"X-USER-TOKEN":os.environ.get("pixela_token")}

# response = requests.post(url=graph_endpoint,json=graph_config, headers=headers)
# print(response.text)
#check the graph
#https://pixe.la/v1/users/a-know/graphs/graph1.html

#Creating an input:/v1/users/<username>/graphs/<graphID>

today = dt.datetime.now()

input_endpoint = "{}/{}/graphs/graph1".format(pixela_endpoint, os.environ.get("pixela_user"))

input_config = {"date":today.strftime("%Y%m%d"), "quantity":input("How many Pushups did you do today? ")}


response = requests.post(url=input_endpoint, headers=headers, json=input_config)
print(response.text)

#update a pixel
update_endpoint = "{}/{}/graphs/graph1/{date}".format(pixela_endpoint, os.environ.get("pixela_user"),date=dt.datetime(year=2021, month=12, day=24).strftime("%Y%m%d"))

update_config = {"quantity":"35"}

# response = requests.put(url=update_endpoint, headers=headers, json=update_config)
# print(response.text)

#delete a pixel

delete_endpoint = "{}/{}/graphs/graph1/{date}".format(pixela_endpoint, os.environ.get("pixela_user"),date=dt.datetime(year=2021, month=12, day=24).strftime("%Y%m%d"))

# response = requests.delete(url=delete_endpoint, headers=headers)
# print(response.text)