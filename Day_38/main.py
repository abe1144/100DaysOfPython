import requests
import os

nutrition_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"

headers = {"x-app-id":os.environ.get("nutritionix_id"),"x-app-key":os.environ.get("nutritionix_key"), "Content-Type": "application/json"}

config = {"query":input("What Exercises did you do today? ")}

response = requests.post(url=nutrition_endpoint, headers=headers, json=config)
print(response.text)