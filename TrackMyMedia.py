# TrackMyMedia
import sqlite3

import requests

import os

from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("OMDB_API_KEY")

conn = sqlite3.connect("media.db") #create database file on your disk
cursor = conn.cursor() # create cursor object. Cursor object acts as the middleware, it allows SQL statements to be executed.

#Triple double quotes create multi-line strings
cursor.execute("""CREATE TABLE IF NOT EXISTS movies( 
               id INTEGER PRIMARY KEY AUTOINCREMENT,
               title TEXT NOT NULL,
               year TEXT,
               genre TEXT,
               rating TEXT)""")

conn.commit() # commit() is like  hitting the "Save" button on a Word document or a video game checkpoint.

print("Database and table initialized successfully!")

# Adding a movie to the database
def add_movie_to_db(title,year,genre,rating):
    cursor.execute(""" INSERT INTO movies (title,year,genre,rating)
    VALUES (?,?,?,?)""",(title,year,genre,rating)) # ? are placeholder values, we use placeholder values to prevent against SQL injection attacks 

    conn.commit()
    print(f"{title} has been successfully added to your watchlist!")

#View all movies from the database
def view_movie_from_db():
    cursor.execute(""" SELECT * FROM movies""")

    # fetchall() grabs all the rows returned by our SQL query as a list of tuples.
    movies = cursor.fetchall()

    if not movies:
        print("\nYour watchlist is currently empty!")
        return

    print("\n---------Your Watchlist---------")
    for movie in movies:
        print(f"[{movie[0]}] {movie[1]} ({movie[2]}) | Genre: {movie[3]} | Rating: {movie[4]}")

    print("-----------------------------------")

def delete_movie_from_db(movieid):
    cursor.execute(""" SELECT * FROM movies WHERE id=?""",(movieid,))
    movie = cursor.fetchone()
    if movie is None:
        print(f"\n❌ Error: No movie found with ID {movieid}.")
        return
    
    cursor.execute("""DELETE FROM movies WHERE id=?""", (movieid,))
    conn.commit()
    print(f"\n🗑️ Successfully deleted '{movie[1]}' (ID: {movieid}) from your watchlist!")


def fetch_movie_from_api(title):
    url = f"http://omdbapi.com?apikey={API_KEY}&t={title}"
    print(f"Connecting to the web to find '{title}'...")
    try:
        response = requests.get(url)

        moviedata = response.json()

        if moviedata.get("Response") == "True":
            title = moviedata.get("Title")
            year = moviedata.get("Year")
            genre = moviedata.get("Genre")
            rating = moviedata.get("imdbRating")

            print("\n🔍 Found matching movie details:")
            print(f"   🎬 Title:  {title}")
            print(f"   📅 Year:   {year}")
            print(f"   🎭 Genre:  {genre}")
            print(f"   ⭐ Rating: {rating}/10")

            confirm = (
                input("\nDo you want to save this to your watchlist? (y/n): ")
                .strip()
                .lower()
            )
            if confirm == "y":
                add_movie_to_db(title, year, genre, rating)
            else:
                print("❌ Movie was not saved.")
        else:
            print(f"\n⚠️ API Error: {moviedata.get('Error')}")
    except requests.exceptions.ConnectionError:
        print("\n🌐 Network error. Please check your internet connection.")


#Main Menu
def mainmenu():
    while True:
        print("\n--- TrackMyMedia Application ---")
        print("1. View Tracked List")
        print("2. Search & Add Movie (Web API)")
        print("3. Delete Movie (By ID)")
        print("4. Exit Program")

        choice = input("\nSelect an option (1-4): ").strip()

        if choice == "1":
            view_movie_from_db()
        elif choice == "2":
            title_input = input("\nEnter the movie title you want to search: ").strip()
            if not title_input:
                print("⚠️ Title cannot be blank.")
                return
            fetch_movie_from_api(title_input)
        elif choice == "3":
            view_movie_from_db()
            try:
                id_to_delete = int(input("\nEnter the ID number to delete: "))
                delete_movie_from_db(id_to_delete)
            except ValueError:
                print("⚠️ Invalid input. Please enter a valid number ID.")
        elif choice == "4":
            print("\n👋 Goodbye! Thanks for tracking your media.")
            break
        else:
            print("⚠️ Invalid choice. Please enter a number between 1 and 4.")

mainmenu()
conn.close()
    
