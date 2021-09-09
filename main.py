import os
import requests
from datetime import datetime

APP_ID = os.environ['APP_ID']
APP_KEY = os.environ['APP_KEY']
AUTHENTICATION = os.environ['AUTHENTICATION']
USERNAME = os.environ['USERNAME']
PASSWORD = os.environ['PASSWORD']

today = datetime.now()

nutritionix_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"

params = {
    "query": input("What did you do today?: "),
    "gender": "male",
    "weight_kg": 95.5,
    "height_cm": 190.0,
    "age": 27
}

headers = {
    "x-app-id": APP_ID,
    "x-app-key": APP_KEY

}

response = requests.post(url=nutritionix_endpoint, json=params, headers=headers)
data = response.json()
exercise_data = data['exercises'][0]
print(exercise_data)

sheety_endpoint = "https://api.sheety.co/09db48d61ff0f61fdf69379d4db0a53e/myWorkouts/workouts"

sheet_params = {
    "workout": {
        "date": today.strftime("%m/%d/%Y"),
        "time": today.strftime("%H:%M:%S"),
        "exercise": exercise_data['name'].capitalize(),
        "duration": exercise_data['duration_min'],
        "calories": exercise_data['nf_calories']
    }
}

response2 = requests.post(url=sheety_endpoint, json=sheet_params, auth=(USERNAME, PASSWORD))
print(response2.text)
