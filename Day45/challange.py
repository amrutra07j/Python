from bs4 import BeautifulSoup
import requests

empire = requests.get("https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/")
movies_html = empire.text
print(movies_html)