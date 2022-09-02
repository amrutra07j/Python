import requests
import datetime as dt

current_date = dt.datetime.now()
date = current_date.strftime('%d/%m/%Y')
time = current_date.strftime('%H:%M:%S')
print(date, time)
# exit()

APP_ID = "7223df1a"
APP_KEY = "0425c0cae38bdb669c441bccfffef953"
API_URL = "https://trackapi.nutritionix.com"

HEADERS_NUTRI = {
    "x-app-id": APP_ID,
    "x-app-key": APP_KEY
}

PARAMS = {
    "query": input("enter your things: "),
    "gender": "male",
    "weight_kg": 75,
    "height_cm": 174,
    "age": 24
}

res_nutri = requests.post(url=f"{API_URL}/v2/natural/exercise", json=PARAMS, headers=HEADERS_NUTRI)
data_nutri = res_nutri.json()
print(data_nutri["exercises"][0])
data_nutri = data_nutri["exercises"][0]

out_diction = {"workout": {}}

out_diction["workout"]["date"] = date
out_diction["workout"]["time"] = time
out_diction["workout"]["exercise"] = data_nutri["name"].title()
out_diction["workout"]["duration"] = data_nutri["duration_min"]
out_diction["workout"]["calories"] = data_nutri["nf_calories"]
print(out_diction)

HEADERS_SHEETY = {
    "Authorization": "Basic bnVsbDpudWxs"
}

url_sheety = "https://api.sheety.co/f4caf79cbf9296ce0534a3fd80edc5fc/myWorkouts/workouts"
res = requests.post(url=url_sheety, json=out_diction, headers=HEADERS_SHEETY)
print(res.text)
# data_work = res.json()
# print(data_work)
