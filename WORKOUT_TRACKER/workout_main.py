import requests
from datetime import datetime
import os

APPID = os.environ.get("APP_ID")
APPKEY = os.environ.get("APP_KEY")
EX_EP = "https://trackapi.nutritionix.com/v2/natural/exercise"
SHEET_EP = os.environ.get("SHEET_ENDPOINT")

ex_input = input("Which exercises you did? ")
exhead = {"x-app-id": APPID, "x-app-key": APPKEY,}
expar = {"query": ex_input, }
exre = requests.post(url=EX_EP, headers=exhead, json=expar, ).json()

date = datetime.now().strftime('%d/%m/%Y')
time = datetime.now().strftime('%I:%M %p')
# Date	Time	Exercise	Duration	Calories
for i in exre["exercises"]:
    sheet_par = {
        "workout": {
            "date": date,
            "time": time,
            "exercise": i["name"].title(),
            "duration": i["duration_min"],
            "calories": i["nf_calories"],
        }
    }
    bearer_headers = {
        "Authorization": f"Bearer {os.environ['TOKEN']}",
    }
    add_sheet = requests.post(url= SHEET_EP, json=sheet_par, headers=bearer_headers)
    print(add_sheet)

