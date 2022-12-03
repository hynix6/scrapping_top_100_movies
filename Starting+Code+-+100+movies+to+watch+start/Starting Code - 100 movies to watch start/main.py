import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

# Write your code below this line 👇
response = requests.get(URL)

movie_webpage = response.text
soup = BeautifulSoup(movie_webpage, "html.parser")
movie_titles = soup.find_all(name="h3", class_="title")
movies_list = [movie.get_text() for movie in movie_titles]
movies = movies_list[::-1]

with open("movies.txt", mode="w") as file:
    for movie in movies:
        file.write(f"{movie}\n")

