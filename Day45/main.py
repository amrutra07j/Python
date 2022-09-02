import copy

from bs4 import BeautifulSoup
import requests

ycomb = requests.get("https://news.ycombinator.com/")
html = ycomb.text

soup = BeautifulSoup(html, "html.parser")
tags = soup.select(".title a")
title_list = []
title_tag = []
score = soup.find_all(name="span", class_="score")
score_list = [int(i.getText().split()[0]) for i in score]
for i in tags:
    if i.get("class") is not None:
        title_list.append(i.getText())
        title_tag.append(i.get("href"))
score_sort = copy.deepcopy(score_list)
score_sort.sort(reverse=True)
# print(title_list)
# print(title_tag)
# print(score_list)
title_list_1 = []
title_tag_1 = []

for i in range(len(score_sort)):
    j = score_list.index(score_sort[i])
    print(j)
    print(title_list[j])
    title_list_1.append(title_list[j])
    title_tag_1.append(title_tag[j])
print(title_list)
print(title_list_1)
print(title_tag_1)
print(score_sort)
print(score_list)

