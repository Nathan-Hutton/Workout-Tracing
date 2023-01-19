import os
import requests
from dotenv import load_dotenv
from datetime import datetime

load_dotenv('/Users/natha/PycharmProjects/info.env')
APPLICATION_KEY = os.getenv('NUTRITION_KEY')
APPLICATION_ID = os.getenv('NUTRITION_ID')
sheety_token = os.getenv('SHEETY_TOKEN')

headers = {
    'x-app-id': APPLICATION_ID,
    'x-app-key': APPLICATION_KEY,
    'Content-Type': 'application/json',
}
exercise_params = {
    'query': input('What exercises did you do today?: '),
    'gender': 'male',
    'weight_kg': 65.7,
    'height_cm': 175,
    'age': 19
}
exercise_endpoint = 'https://trackapi.nutritionix.com/v2/natural/exercise'
response = requests.post(url=exercise_endpoint, json=exercise_params, headers=headers)
data = response.json()
# print(data)

date = datetime.now().strftime('%Y/%m/%d')
time = datetime.now().strftime("%X")
sheety_params = {
    'workout': {
        'exercise': data['exercises'][0]['name'],
        'date': date,
        'time': time,
        'duration': data['exercises'][0]['duration_min'],
        'calories': data['exercises'][0]['nf_calories']
    }
}
sheety_headers = {
    'Authorization': 'Bearer odonaglnsonosanga3',
    "Content-Type": "application/json"
}
sheety_endpoint = 'https://api.sheety.co/721787b36264afa0d16fea5cc6a74cc1/workoutTracking/workouts'

# response = requests.post(url=sheety_endpoint, json=sheety_params, headers=sheety_headers)

