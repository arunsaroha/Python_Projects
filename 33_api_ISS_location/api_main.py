import time

import requests
from datetime import datetime

MY_LAT = 30.4724
MY_LNG = 76.4312

def is_night():
    parameters = {
        "lat":MY_LAT,
        "lng":MY_LNG,
        "formatted": 0,
    }
    response = requests.get("http://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    time_now = datetime.now().hour

    if time_now >= sunset or time_now <= sunrise:
        return True

def is_iss_overhead():
    response_iss = requests.get(url="http://api.open-notify.org/iss-now.json")
    response_iss.raise_for_status()
    data_iss = response_iss.json()["iss_position"]
    iss_latitude = float(data_iss["latitude"])
    iss_longitude = float(data_iss["longitude"])
    if MY_LAT-5 <= iss_latitude <= MY_LAT+5 and MY_LNG-5 <= iss_longitude <= MY_LNG+5:
        return True

while True:
    time.sleep(60)
    if is_iss_overhead() and is_night():
        print("LOOK UP, :) WAVE TO THE ISS")