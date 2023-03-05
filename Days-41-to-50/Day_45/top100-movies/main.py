import requests
from bs4 import BeautifulSoup

URL = 'https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/'

response = requests.get(URL)
empire_web_page = response.text

soup = BeautifulSoup(empire_web_page, 'html.parser')
movie_titles = [title.getText() for title in soup.find_all(name='h3', class_='title')]

with open('movies.txt', mode='w', encoding='utf8') as file:
    for title in movie_titles[::-1]:
        file.write(f'{title}\n')
