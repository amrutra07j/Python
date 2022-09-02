import datetime as dt
import requests
from twilio.rest import Client

STOCK = "FB"
COMPANY_NAME = "Facebook"

# STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").
# import csv
today = dt.date.today()
yesterday = str(today - dt.timedelta(days=2))
day_before_yesterday = str(today - dt.timedelta(days=2))
print(yesterday)

STOCK_PARAMETERS = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK,
    "apikey": "YKK5T2SSBPYDLJFJ"
}

NEWS_PARAMETERS = {
    "apikey": "f43795b70175491e965f7852bb030350",
    "qInTitle": COMPANY_NAME,
    "from": yesterday,
    "sortBy": "popularity"
}
session = requests.get("https://www.alphavantage.co/query?", params=STOCK_PARAMETERS)
session.raise_for_status()
data = session.json()
yesterday_price = float(data["Time Series (Daily)"][yesterday]["4. close"])
day_before_yesterday_price = float(data["Time Series (Daily)"][day_before_yesterday]["4. close"])
percent_decline_increase = round((yesterday_price - day_before_yesterday_price) / yesterday_price * 100, 2)
# STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME.
if abs(percent_decline_increase) < 5:
    session = requests.get("https://newsapi.org/v2/everything?", params=NEWS_PARAMETERS)
    articles = session.json()['articles'][:3]
    # STEP 3: Use https://www.twilio.com
    # Send a seperate message with the percentage change and each article's title and description to your phone number.
    account_sid = "ACbf1a66a74ba7569c49b374179ee35329"
    auth_token = "95ac8461a86c673fbf6a8dc6c953b842"
    for article in articles:
        print(f"{STOCK}: {percent_decline_increase}\nHeadline: {article['title']}\nBrief: {article['description']}")
        client = Client(account_sid, auth_token)
        message = client.messages \
            .create(
            body=f"{STOCK}: {percent_decline_increase}\nHeadline: {article['title']}\nBrief: {article['description']}",
            from_='++16204904995',
            to='+919513147686'
        )

# Optional: Format the SMS message like this:
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""
