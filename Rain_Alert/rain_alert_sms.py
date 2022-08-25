import requests
from twilio.rest import Client

api = "https://api.openweathermap.org/data/2.5/forecast"
api_key = "a52d572e523a150e0a74d5f96b66bd52"
account_sid = "AC4d7e9677916f84410cf37539fe2706b4"
auth_token = "4e441b803a44780679b3bc1d42275642"

parameters = {
    "lat": 30.115990,
    "lon": 77.286903,
    "appid": api_key,
}
response = requests.get(url=api, params=parameters)
response.raise_for_status()
weather_data = response.json()
weather_slice = weather_data["list"][:4]
will_rain = False

for i in weather_slice:
    condition_code = i["weather"][0]["id"]
    if int(condition_code) < 600:
        will_rain = True

if will_rain:
    client = Client(account_sid, auth_token)

    message = client.messages.create(
        body="Hello Mummy Ji, message aaya ho to phone krna, main project bana rha hun😁😁",
        from_="+16405003215",
        to="+919115572874"
    )

    print(message.status)
