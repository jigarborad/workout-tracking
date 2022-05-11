import requests
from datetime import datetime
import os
API_ID = os.environ['API_ID']
API_KEY = os.environ['API_ID']
TOKEN = os.environ['TOKEN']

GENDER = "male"
WEIGHT_KG = 55
HEIGHT_CM = 160
AGE = 22

headers = {
    "x-app-id": API_ID,
    "x-app-key": API_KEY,
    "x-remote-user-id": "0",
}
exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
exercise_text = input("Tell me which exercises you did: ")
parameters = {
    "query": exercise_text,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE,
}

response = requests.post(url=exercise_endpoint, json=parameters, headers=headers)
result = response.json()

today_date = datetime.now()
sheety_endpoint = os.environ['sheety_endpoint']
headers_sheety = {
    "Authorization": f"Bearer {TOKEN}"
}
for exercise in result["exercises"]:
    sheety_parameters = {
        "workout": {
            "date": today_date.strftime("%d/%m/%Y"),
            "time": today_date.strftime("%X"),
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }
    sheety_response = requests.post(url=sheety_endpoint,json=sheety_parameters, headers= headers_sheety)
    print(sheety_response.text)