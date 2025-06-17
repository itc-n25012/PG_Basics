import csv

movies = [
        ["トップガン", "卒業白書", "マイノリティ・リポート"],
        ["タイタニック", "レヴェナント", "フライト"]
        ]

with open("movie_ja.csv", "w", encoding="utf-8") as f:
    w = csv.writer(f, delimiter=",")
    for movie in movies:
        w.writerow(movie)
