import requests

LAT = 15.638385
LONG = 75.947680

PARAMETERS = {
    "lat": 15.638385,
    "long": 75.947680,
    "formatted": 0
}

response = requests.get(url="https://api.sunrise-sunset.org/json", params=PARAMETERS)
response.raise_for_status()

data = response.json()
sunrise = data["results"]["sunrise"]
sunset = data["results"]["sunset"]

print(sunrise, sunset)