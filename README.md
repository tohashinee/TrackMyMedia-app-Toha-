**# TrackMyMedia — CLI Movie Watchlist Application**



A Python Command Line Interface (CLI) application designed to log, track, and manage a movie watchlist. This project moves away from ephemeral in-memory storage by implementing persistent local database storage and integrates with a external live Web API to automate information discovery.



**## 🚀 Key Features**



Persistent Storage (SQLite): Leverages a robust local relational database engine via SQLite to enable persistent CRUD workflows (Create, Read, Delete) so user lists remain saved indefinitely on disk.

Automated Data Enrichment (OMDb Web API):Dynamically calls an external REST API using `requests` to fetch data fields (Release Year, Genre, IMDb Rating) using only a movie title.

Input Validation \& Crash Prevention: Standardizes error blocks handling API connection drops, empty field queries, structural typing inputs, and "Movie Not Found" returns gracefully without terminating execution loops.

Environment Security Configuration: Securely handles authentication API credentials utilizing externalized `.env` parameters away from the public source code repository.



**## 🛠️ Built With**



Python 3

SQLite3 (Native built-in database module)

Requests (HTTP client for querying RESTful API endpoints)

Python-dotenv (Environment variable tracking configuration management)



**## 📋 Installation \& Local Setup**



Follow these steps to set up and execute the application locally:



\### 1. Clone the Repository

```bash

git clone https://github.com

cd TrackMyMedia-app-Toha-

```



\### 2. Install Project Dependencies

Ensure dependencies are fetched using pip:

```bash

pip install requests python-dotenv

```



\### 3. Configure Environment Credentials

1\. Obtain a free API configuration key from \[OMDb API](https://omdbapi.com).

2\. Create a new file named `.env` in the root of your project directory.

3\. Save your credentials inside it using the exact variable mapping pattern:

```text

OMDB\_API\_KEY=your\_private\_api\_key\_here

```



\### 4. Run the Application

Execute the primary execution script to launch the application interface:

```bash

python TrackMyMedia.py

```



\## 🧠 What I Learned From This Project



Database Lifecycle Routines: Learned how pointers (cursors) interface with local databases, structuring table creation scripts, utilizing variables safely via sanitized query parameter placeholders `?` to mitigate SQL injection vulnerabilities, and implementing disk commit cycles `conn.commit()`.

REST API Networking: Learned how structured parameters interact across URLs (`?apikey=` and `\&t=`), unpacking asynchronous web JSON responses inside data frames, and managing network failures dynamically.

\* \*\*Production Security Fundamentals:\*\* Understood Git workflow protection behaviors by employing standard targeting guidelines within `.gitignore` layers to drop tracking dependencies for personal active files like local databases and application keys.



