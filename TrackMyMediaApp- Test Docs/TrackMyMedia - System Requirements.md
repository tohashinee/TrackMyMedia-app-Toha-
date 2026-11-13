TrackMyMedia - System Requirements Specification



**Project Overview**



TrackMyMedia is a Python Command-Line Interface (CLI) application designed to automate multimedia tracking. It eliminates manual data entry by fetching real-time metadata from the external OMDb REST API and ensures data persistence using a local SQLite relational database.



**Functional Requirements**

FR-01 (API Search): The system shall allow users to search for movies by title via the OMDb REST API and display the Title, Release Year, Genre, and IMDb Rating.

FR-02 (User Confirmation): The system shall prompt the user to confirm (`y/n`) before committing fetched API data to the database.

FR-03 (Persistent Storage): The system shall store confirmed movie records permanently in a local SQLite database (`media.db`).

FR-04 (View Watchlist): The system shall retrieve and display all saved movies along with their unique database IDs.

FR-05 (Delete Record): The system shall allow users to remove a movie from the database using its unique ID.



**Non-Functional Requirements**

NFR-01 (Security - Credential Protection): API keys must be stored in an external `.env` file and excluded from version control via `.gitignore`.

NFR-02 (Security - Injection Mitigation): All database queries must utilize parameterized placeholders (`?`) to prevent SQL injection attacks.

NFR-03 (Reliability \& Error Handling): The application must gracefully catch network timeouts, invalid API responses, and non-numeric menu inputs without crashing.

NFR-04 (Responsiveness): External API calls should use a defined timeout so the application does not wait indefinitely.





&#x20;



&#x20;

