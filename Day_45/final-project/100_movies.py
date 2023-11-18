import requests
from bs4 import BeautifulSoup
import codecs

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

response = requests.get(URL)
response.raise_for_status()

movies_webpage = response.text

soup = BeautifulSoup(movies_webpage, 'html.parser')

all_movies = soup.find_all(name="h3", class_="title")
movie_titles = [title.getText() for title in all_movies]
#print(sorted(movie_titles))
print(movie_titles[::-1])

with codecs.open('movies.txt', mode='w', encoding='utf-8') as file:
    for movie in movie_titles:
        file.write(f"{movie}\n")



