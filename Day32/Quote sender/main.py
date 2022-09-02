import random
import smtplib
import datetime as dt

G_EMAIL = "udemyt07@gmail.com"
Y_EMAIL = "udemyt07@yahoo.com"
PASSWORD = "Tyrion@07"
Y_PASSWORD = "xmztmmahhsfnmboj"
DAYS_LIST = ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"]

now = dt.datetime.now()
day = now.weekday()
if day == 1:
    with open("quotes.txt") as file:
        quote = random.choice(file.readlines())[:-1]

    with smtplib.SMTP("smtp.mail.yahoo.com", port=587) as connection:
        connection.starttls()
        connection.login(user=Y_EMAIL, password=Y_PASSWORD)
        connection.sendmail(from_addr=Y_EMAIL, to_addrs=G_EMAIL, msg=f"Subject:Ignite Yourself\n\n{quote}")



