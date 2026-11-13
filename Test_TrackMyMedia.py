import io
import sqlite3
import unittest
from unittest.mock import MagicMock, patch
import requests
import TrackMyMedia as app


class TestTrackMyMedia(unittest.TestCase):
    def setUp(self):
        """Creates a fresh in-memory SQLite database before each test case."""
        self.conn = sqlite3.connect(":memory:")
        self.cursor = self.conn.cursor()
        self.cursor.execute("""
            CREATE TABLE movies(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT NOT NULL,
                year TEXT,
                genre TEXT,
                rating TEXT
            )
        """)
        self.conn.commit()
        app.conn = self.conn
        app.cursor = self.cursor

    def tearDown(self):
        """Closes the temporary test database after each test case."""
        self.conn.close()

    # TC-01 | TS-01 | FR-01, FR-02, FR-03
    @patch("requests.get")
    def test_tc01_search_and_save_valid_movie(self, mock_get):
        mock_resp = MagicMock()
        mock_resp.json.return_value = {
            "Response": "True",
            "Title": "Inception",
            "Year": "2010",
            "Genre": "Action, Adventure, Sci-Fi",
            "imdbRating": "8.8",
        }
        mock_get.return_value = mock_resp

        with patch("builtins.input", side_effect=["2", "Inception", "y", "4"]), \
             patch("sys.stdout", new_callable=io.StringIO) as fake_out:
            app.mainmenu()
            output = fake_out.getvalue()

        self.assertIn("Inception", output)
        self.assertIn("2010", output)
        self.assertIn("Inception has been successfully added to your watchlist!", output)

        self.cursor.execute("SELECT title, year, genre, rating FROM movies")
        rows = self.cursor.fetchall()
        self.assertEqual(len(rows), 1)
        self.assertEqual(rows[0], ("Inception", "2010", "Action, Adventure, Sci-Fi", "8.8"))

    # TC-02 | TS-01 | FR-02
    @patch("requests.get")
    def test_tc02_decline_saving_fetched_movie(self, mock_get):
        mock_resp = MagicMock()
        mock_resp.json.return_value = {
            "Response": "True",
            "Title": "Interstellar",
            "Year": "2014",
            "Genre": "Adventure, Drama, Sci-Fi",
            "imdbRating": "8.7",
        }
        mock_get.return_value = mock_resp

        with patch("builtins.input", side_effect=["2", "Interstellar", "n", "4"]), \
             patch("sys.stdout", new_callable=io.StringIO) as fake_out:
            app.mainmenu()
            output = fake_out.getvalue()

        self.assertIn("Movie was not saved.", output)
        self.cursor.execute("SELECT COUNT(*) FROM movies")
        self.assertEqual(self.cursor.fetchone()[0], 0)

    # TC-03 | TS-02 | FR-04
    def test_tc03_view_watchlist_with_existing_data(self):
        app.add_movie_to_db("Inception", "2010", "Sci-Fi", "8.8")
        app.add_movie_to_db("The Matrix", "1999", "Action", "8.7")

        with patch("builtins.input", side_effect=["1", "4"]), \
             patch("sys.stdout", new_callable=io.StringIO) as fake_out:
            app.mainmenu()
            output = fake_out.getvalue()

        self.assertIn("[1] Inception (2010) | Genre: Sci-Fi | Rating: 8.8", output)
        self.assertIn("[2] The Matrix (1999) | Genre: Action | Rating: 8.7", output)

    # TC-04 | TS-03 | FR-05
    def test_tc04_delete_existing_movie_by_valid_id(self):
        app.add_movie_to_db("Inception", "2010", "Sci-Fi", "8.8")

        with patch("builtins.input", side_effect=["3", "1", "4"]), \
             patch("sys.stdout", new_callable=io.StringIO) as fake_out:
            app.mainmenu()
            output = fake_out.getvalue()

        self.assertIn("Successfully deleted 'Inception' (ID: 1)", output)
        self.cursor.execute("SELECT COUNT(*) FROM movies")
        self.assertEqual(self.cursor.fetchone()[0], 0)

    # TC-05 | TS-03 | FR-05
    def test_tc05_delete_nonexistent_movie_id(self):
        with patch("builtins.input", side_effect=["3", "9999", "4"]), \
             patch("sys.stdout", new_callable=io.StringIO) as fake_out:
            app.mainmenu()
            output = fake_out.getvalue()

        self.assertIn("No movie found with ID 9999", output)

    # TC-06 | TS-04 | NFR-03
    def test_tc06_invalid_cli_menu_choice(self):
        with patch("builtins.input", side_effect=["hello", "4"]), \
             patch("sys.stdout", new_callable=io.StringIO) as fake_out:
            app.mainmenu()
            output = fake_out.getvalue()

        self.assertIn("Invalid choice. Please enter a number between 1 and 4.", output)

    # TC-07 | TS-04 | NFR-03, NFR-04
    @patch("requests.get", side_effect=requests.exceptions.Timeout("Connection timed out"))
    def test_tc07_api_timeout_and_network_failure(self, mock_get):
        with patch("sys.stdout", new_callable=io.StringIO) as fake_out:
            app.fetch_movie_from_api("Inception")
            output = fake_out.getvalue()

        self.assertTrue("timed out" in output.lower() or "network error" in output.lower())

    # TC-08 | TS-05 | NFR-02
    def test_tc08_sql_injection_payload_mitigation(self):
        malicious_payload = "'; DROP TABLE movies;--"
        app.add_movie_to_db(malicious_payload, "2024", "Test", "5.0")

        self.cursor.execute("SELECT title FROM movies")
        result = self.cursor.fetchone()
        self.assertIsNotNone(result)
        self.assertEqual(result[0], malicious_payload)


if __name__ == "__main__":
    unittest.main(verbosity=2)
