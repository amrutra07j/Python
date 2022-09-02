import requests
import os
from twilio.rest import Client
from twilio.http.http_client import TwilioHttpClient

PARAMETERS = {
    "lat": -19.830500,
    "lon": 34.843021,
    "exclude": "current,minutely,daily",
    "appid": "3187c93a31c2ca7adad3179663ed5255"
}

response = requests.get(url="https://api.openweathermap.org/data/2.5/onecall?", params=PARAMETERS)
response.raise_for_status()
data = response.json()
count = 0
weather_12 = data["hourly"][:12]
is_weather = False
for details in weather_12:
    if details["weather"][0]["id"] < 700:
        is_weather = True
        # print(f"{details['weather'][0]['id']}: Bring your umbrella")

if is_weather:
    print("Useless fellow bring Umbrella")
    # proxy_client = TwilioHttpClient()
    # proxy_client.session.proxies = {'https': os.environ['https_proxy']}
    account_sid = "ACbf1a66a74ba7569c49b374179ee35329"
    auth_token = "95ac8461a86c673fbf6a8dc6c953b842"
    client = Client(account_sid, auth_token)

    message = client.messages \
        .create(
        body="Useless fellow bring Umbrella",
        from_='++16204904995',
        to='+919513147686'
    )

    print(message.sid)