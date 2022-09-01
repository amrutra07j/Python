import requests
from bs4 import BeautifulSoup

site = requests.get("https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/")
soup = BeautifulSoup(site.text, "html.parser")
movie_list_html = soup.find_all('h3','title')
movie_list = []
for movie in movie_list_html:
    movie_list.append(movie.getText())



with open('movies.txt', 'w') as movie_file:
    for i in range(len(movie_list) - 1, -1, -1):
        movie_file.write(f'{movie_list[i]}\n')

