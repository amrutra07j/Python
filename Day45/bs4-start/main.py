from bs4 import BeautifulSoup

with open("website.html", encoding="utf-8") as file:
    data = file.read()
soup = BeautifulSoup(data, "html.parser")

elements = soup.find_all(name="a")
print(elements)
for element in elements:
    print(element.get("href"))
#
headings = soup.find_all(name="h1", id="name")
# print(headings)
for heading in headings:
    print(heading.string)

headings = soup.select_one(selector="p a").getText()
print(headings)
# import requests
#
# res = requests.get("https://mail.google.com/mail/u/1/#inbox/FMfcgzGmthgmlJthxChQdVBnlnHQrmQg")
# print(res.json())
#
# res.raise_for_status()