import requests
import datetime

NUTRITION_APPLICATION_ID = "e667d8a8"
NUTRITION_KEY = "b4c8aac28326ce4f101757d1b822bc4a"
NUTRITION_END_POINT = "https://trackapi.nutritionix.com/v2/natural/exercise"

SHEET_ENDPOINT = "https://api.sheety.co/5b6677c703d1b1b5dfb0ec3fc093fde8/pythonFitness/лист1"

SHEET_AUTH_BEARER = "Bearer bbsecrettokenmuhahaha"

nutri_header = {
    "x-app-id": NUTRITION_APPLICATION_ID,
    "x-app-key": NUTRITION_KEY,
}


nutri_exercise = {
    "query": input("Tell me which exercise you did?\n")
}

respond_exercises = requests.post(NUTRITION_END_POINT, headers=nutri_header, json=nutri_exercise)
exercises = respond_exercises.json()["exercises"]

sheet_header = {
    "Authorization": SHEET_AUTH_BEARER,
}

today_date = datetime.datetime.now().strftime("%d/%m/%Y")
today_time = datetime.datetime.now().strftime("%X")
for exer in exercises:
    sheet_params = {
        "лист1": {
            "date": today_date,
            "time": today_time,
            "exercise": exer["name"].title(),
            "duration": f"{exer['duration_min']}min",
            "calories": exer["nf_calories"],
        },
    }
    upload_data = requests.post(url=SHEET_ENDPOINT, json=sheet_params, headers=sheet_header)
    print(upload_data.status_code)
