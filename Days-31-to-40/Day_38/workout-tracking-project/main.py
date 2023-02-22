import os
import requests
from datetime import datetime

NUTRITIONIX_APP_ID = os.environ['NUTRITIONIX_APP_ID']
NUTRITIONIX_APP_KEY = os.environ['NUTRITIONIX_APP_KEY']
NUTRITIONIX_ENDPOINT = 'https://trackapi.nutritionix.com/v2/natural/exercise'

SHEETY_BEARER_TOKEN = os.environ['SHEETY_BEARER_TOKEN']
SHEETY_POST_ENDPOINT = 'https://api.sheety.co/b70343d18fb5bf9c870e534c1d4bc379/workoutTracking/workouts'

headers = {
    'x-app-id': NUTRITIONIX_APP_ID,
    'x-app-key': NUTRITIONIX_APP_KEY
}

user_answer = input('Tell me what exercises you did today: ')

workout_description = {
 "query": user_answer
}

response = requests.post(url=NUTRITIONIX_ENDPOINT, json=workout_description, headers=headers)
response.raise_for_status()

exercises_details = response.json()['exercises']

today = datetime.now()

date = f'{today.strftime("%d")}/{today.strftime("%m")}/{today.strftime("%Y")}'
time = today.strftime("%X")

headers = {
    'Authorization': SHEETY_BEARER_TOKEN
}

for exercise in exercises_details:
    exercise_name = exercise['name'].title()
    duration = exercise['duration_min']
    burned_calories = exercise['nf_calories']

    row_data = {
        'workout': {
            'date': date,
            'time': time,
            'exercise': exercise_name,
            'duration': duration,
            'calories': burned_calories
        }
    }

    response = requests.post(url=SHEETY_POST_ENDPOINT, json=row_data, headers=headers)
    response.raise_for_status()
