
from bs4 import BeautifulSoup
import requests

response = requests.get(url="https://www.empireonline.com/movies/features/best-movies-2/")

web_page = response.text

soup = BeautifulSoup(web_page, "html.parser")

movies = soup.find_all(name="h3", class_="listicleItem_listicle-item__title__BfenH")

movie_list = [cinema.text for cinema in movies]

movie_list.reverse()

with open("movies.txt", "w", encoding="UTF-8 ") as file:

    for movie in movie_list:

        file.write(f"{movie}\n")
