import csv
import sqlite3


def main():
    #create the database
    open(f"large/movies.db","w").close()
    #create tables
    db = sqlite3.connect("movies.db")
    with open("large/movies.csv", "r") as movies:
        reader = csv.DictReader(movies)
        for row in reader:
            title = row["title"]
            id = int(row["id"])
            year = int(row["year"])
            db.execute("INSERT INTO movies (movieid, title, year) VALUES (?,?,?)", (id, title, year) )
    db.commit()
    db.close()


main()