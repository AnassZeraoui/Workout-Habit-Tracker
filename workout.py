# don't know what to do with this script , read the README file.
import requests
import datetime as dt

gender = "" # type your gender
weight_kg =  # type your weight on Kg
height_cm =  # type your height "cm" only
age =   # type your age

# getting both date and time from the datetime module
date = dt.datetime.now().strftime("%d/%m/%Y")
time = dt.datetime.now().strftime("%I:%M:%S")

# nutritionix required parameters
application_id = ""  # your application_id from the nutritionix account that you've created
nutrition_key = "" # your api key from the nutritionix account that you've created
nutritionix_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"

header = {
    "x-app-id": application_id,
    "x-app-key": nutrition_key,
    "Content-Type": "application/json"
}
parameters = {
    "query": input("What did you exercise today ?:"), # example: i run for 10 miles  , i go to the gym for 2 hours ..
    "gender": gender,
    "weight_kg": weight_kg,
    "height_cm": height_cm,
    "age": age
}
get_infos = requests.post(url=nutritionix_endpoint, headers=header, json=parameters)
result = get_infos.json()
# adding a row:
for exercise in result["exercises"]:
    sheet_inputs = {
        "workout": {
            "date": date,
            "time": time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }

sheety_endpoint = "https://api.sheety.co/ed4cab757dce802d5776cc00391a7a2c/workout/workouts"
requests = requests.post(url=sheety_endpoint, json=sheet_inputs)
print(f"Successful Request :{requests.status_code}")
