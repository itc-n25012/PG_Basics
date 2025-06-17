import csv

movies = [
        ["Top Gun", "Risky Busines", "Minority Report"],
        ["Titanic", "The Revenant", "Inception"],
        ["Training Day", "Man on Fire", "Flight"]]


with open("movie.csv", "w") as f:
    w = csv.writer(f, delimiter=",")
    for movie in movies:
        w.writerow(movie)
