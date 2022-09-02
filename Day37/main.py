import datetime as dt

import requests

TOKEN = "cfgdsersh567"
GRAPH_ID = "a07"
USER_NAME = "amrutraj"
PIX_API = "https://pixe.la/"

# USER_PARAMS = {
#     "token": TOKEN,
#     "username": USER_NAME,
#     "agreeTermsOfService": "yes",
#     "notMinor": "yes"
# }
# res = requests.post(url=f"{PIX_API}v1/users", json=USER_PARAMS)
# print(res.text)

# GRAPH_PARAMS = {
#     "id": "a07",
#     "name": "no_of_pages",
#     "unit": "numbers",
#     "type": "int",
#     "color": "sora"
# }
#
USER_TOKEN = {
    "X-USER-TOKEN": TOKEN
}
#
# res = requests.post(url=f"{PIX_API}v1/users/{USER_NAME}/graphs", json=GRAPH_PARAMS, headers=USER_TOKEN)
# print(res.text)

date = dt.datetime(year=2022, month=1, day=24)

PIXEL_PARAMS = {
    "date": date.strftime("%Y%m%d"),
    "quantity": input(f"number of pages you read on {date.strftime('%d/%m/%Y')}:  "),
    # "optionalData": "BTC"
}

res = requests.post(url=f"{PIX_API}v1/users/{USER_NAME}/graphs/{GRAPH_ID}", json=PIXEL_PARAMS, headers=USER_TOKEN)
print(res.text)

# UPDATE_PIXEL_PARAMS = {
#     "quantity": "05"
# }
#
# res = requests.put(url=f"{PIX_API}v1/users/{USER_NAME}/graphs/{GRAPH_ID}/{date.strftime('%Y%m%d')}", json=UPDATE_PIXEL_PARAMS, headers=USER_TOKEN)
# print(res.text)

# res = requests.delete(url=f"{PIX_API}v1/users/{USER_NAME}/graphs/{GRAPH_ID}/{date.strftime('%Y%m%d')}", headers=USER_TOKEN)
# print(res.text)
