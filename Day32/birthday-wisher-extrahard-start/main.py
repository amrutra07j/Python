##################### Extra Hard Starting Project ######################
import datetime as dt
import random
import pandas
import smtplib
# 1. Update the birthdays.csv
# 2. Check if today matches a birthday in the birthdays.csv
GMAIL = "udemyt07@gmail.com"
YMAIL = "udemyt07@yahoo.com"
PASSWORD = "Tyrion@07"
now = dt.datetime.now()
month = now.month
day = int(now.day)
birthday_data = pandas.read_csv("birthdays.csv")
for (index, row) in birthday_data.iterrows():
    if row.month == month and row.day == day:
# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv
        with open(f"letter_templates/letter_{random.randint(1, 3)}.txt") as letter:
            letter_data = letter.read()
            letter_data = letter_data.replace("[NAME]", row["name"])
# 4. Send the letter generated in step 3 to that person's email address.
        with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
            connection.starttls()
            connection.login(user=GMAIL, password=PASSWORD)
            connection.sendmail(from_addr=GMAIL, to_addrs=row["email"], msg=f"Subject:Birthday Wishes\n\n{letter_data}")



