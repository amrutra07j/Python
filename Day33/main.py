import smtplib

import requests
import datetime as dt


G_EMAIL = "udemyt07@gmail.com"
Y_EMAIL = "udemyt07@yahoo.com"
PASSWORD = "Tyrion@07"
Y_PASSWORD = "xmztmmahhsfnmboj"


LAT = 15.638385
LONG = 75.947680

PARAMETERS = {
    "lat": 15.638385,
    "long": 75.947680,
    "formatted": 0
}

def iss_with_us():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()

    data = response.json()
    print(data)
    latitude = float(data["iss_position"]["latitude"])
    longitude = float(data["iss_position"]["longitude"])

    if latitude + 5 >= LAT >= latitude - 5 and longitude + 5 >= LONG >= longitude - 5:
        return True

def night():
    if iss_with_us():
        response = requests.get(url="https://api.sunrise-sunset.org/json", params=PARAMETERS)
        response.raise_for_status()

        data = response.json()
        sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
        sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])
        hour = dt.datetime.now().hour
        if hour < sunrise or hour > sunset:
            print("night")
            return True

if iss_with_us() and night():
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        print("mail")
        connection.starttls()
        connection.login(user=G_EMAIL, password=PASSWORD)
        connection.sendmail(from_addr=G_EMAIL, to_addrs=G_EMAIL,
                        msg="Subject:ISS on your head\n\nWatch ISS satellite now you idiot")
# print(sunrise, sunset)
