TrackMyMedia - Test Scenarios and Test Cases 



Test Scenarios give a high-level idea of what to test while test cases provide detailed step-by-step instructions on how to test.



1. **Test Scenarios**

&#x20;

|Scenario\_ID|Requirement\_ID|Test Scenario Description|Coverage Area|
|-|-|-|-|
|TS-01|FR-01,FR-02,FR-03|Verify searching for a movie via the external OMDb API and saving confirmed results to SQLite. |Positive and Negative Flows|
|TS-02|FR-04|Verify retrieving and displaying all tracked movies from the local database. |Data Integrity and Empty State|
|TS-03|FR-05|Verify deleting tracked movies using their unique database ID. |Positive and Boundary Edges|
|TS-04|NFR-03,NFR-04|Verify graceful error handling during invalid CLI inputs, API errors, and network timeouts.|Resilience \& Fault Tolerance|
|TS-05|NFR-01,NFR-02|Verify security controls against SQL injection payloads and credential leaks in version control.|Security and Compliance|



**2. Test Cases**



|TestID|Secenario\_ID|Requirement\_ID|Test Case Title|Preconditions|Test Steps|Expected Results|Status|
|-|-|-|-|-|-|-|-|
|TC-01|TS-01|FR-01,FR-02,FR-03|Search and Save valid movie|1. Valid API Key in .env<br />2.Active internet<br />3.Test DB ready|1. Select option '2' (Search)<br />2. Enter "Inception"<br />3. Enter 'y' at confirmation point|API displays Title, Year (`2010`), Genre, and Rating; record is committed to SQLite; success message shown. |Pass|
|TC-02|TS-01|FR-02|Decline Saving Fetched Movie|1. Valid API Key configured.<br />2. Active Internet|1. Select option '2' (Search)<br />2. Enter "Interstellar"<br />3. Enter 'n' at confirmation point|App prints `"Movie was not saved";SQLite table row count remains unchanged.|Pass|
|TC-03|TS-02|FR-04|View Watchlist with Existing Data|Test DB contains at least 2 movie records|1. Select option '1' (View Watchlist)|All stored movies print cleanly with their corresponding ID, Title, Year, Genre, and Rating. |Pass|
|TC-04|TS-03|FR-05|Delete Existing Movie by Valid ID|Movie with ID '1' exists in the test DB.|1. Select Option `3` (Delete). 2. Enter ID "1".|Record ID '1' is deleted from SQLite; confirmation message displayed. |Pass|
|TC-05|TS-03|FR-05|Delete Non-Existent Movie ID (Boundary|Movie ID '9999' does not exist in test DB|1. Select Option `3` (Delete). 2. Enter ID "9999".|App displays "No movie found with ID 9999"; database remains unaffected. |Pass|
|TC-06|TS-04|NFR-03|Invalid CLI Menu Choice|Application is at the main menu loop. |1. Enter "hello" at main menu.|App catches invalid choices, prints user-friendly warnings, and returns to the menu. |Pass|
|TC-07|TS-04|NFR-03,NFR-04|API Timeout / Network Failure (Mocked)|requests.get mocked to raise Timeout / ConnectionError|1. Trigger movie lookup function|Exception is caught cleanly; network error prompt is shown without crashing the CLI. |Pass|
|TC-08|TS-05|NFR-02|SQL Injection Payload Mitigation|Test DB initialized with "movies" table. |1. Pass "'; DROP TABLE movies;--" as movie title into add\_movie\_to\_db(). |Parameterized '?'query treats payload as literal text; 'movies' table remains intact.|Pass|



