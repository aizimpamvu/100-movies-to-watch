import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

# Write your code below this line 👇
response = requests.get(URL)

# movie web page

mv_web_page =response.text

soup = BeautifulSoup(mv_web_page, "html.parser")

movies_list = []
all_movies = soup.find_all(name="h3", class_="title")

for movie in all_movies:
    # print(movie.getText())
    with open("movies.txt", "w", encoding="utf8") as file:
        file.write(movie.getText())

