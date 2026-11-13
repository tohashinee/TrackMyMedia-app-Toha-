&#x20;**Software Test Plan — TrackMyMedia**



1. **Objective**



The objective of this test plan is to define the testing strategy, scope, environment, and quality criteria for TrackMyMedia. This plan ensures that all Functional Requirements (`FR-01` through `FR-05`) and Non-Functional Requirements (`NFR-01` through `NFR-04`) are thoroughly verified before deployment.





**2. Scope**

&#x20;

*2.1 In-Scope*



Functional testing of view, search, add and delete workflows.



Positive, negative, boundary, and input-validation testing.



Database persistence and data-integrity checks.



External API response handling, including no-match and connection/request failures.



Basic regression testing after selected defects are fixed.



Selected automated unit or integration tests using unittest or pytest, where practical.



*2.2 Out-of-Scope*



Testing OMDb internal systems or guaranteeing its service availability.



High-volume load, stress, endurance, or benchmark testing.



Formal penetration testing, vulnerability assessment, or security certification.





**3. Test Strategy and Levels**



|Test type/ Level |Application|Test Approach|
|-|-|-|
|Functional |View, search, add, and delete movies.|Execute requirement-based test cases with controlled inputs.|
|Negative|Blank movie titles, invalid menu choices, no search match|Supply invalid or unexpected input and verify graceful handling.|
|Boundary|Supply invalid or unexpected input and verify graceful handling.|Test valid and invalid edges identified from implementation.|
|Integration|Python application, OMDb API and SQLite|Verify interactions; use controlled/stubbed API responses where feasible.|
|Data Integrity|Insert, retrieve, delete, duplicate handling|Inspect database state before and after operations|
|Regression|Previously tested workflows after a code change|Re-run impacted and critical-path cases.|
|Automated|Pure functions and selected database/API paths|Use unittest or pytest; isolate external dependencies.|





**4. Test Environment \& Tools**



Programming Language: Python 3.14.3

Testing Framework: pytest

Database Engine: SQLite3

IDE: Microsoft Visual Studio

Operating System: Windows



**5. Entry and Exit Criteria** 



*Entry Criteria*



A reviewed source-code version is available, and its version/commit is recorded.



Requirements and expected behaviour are reviewed and baselined for the test cycle.



Python and required dependencies are installed.



A separate test database is configured and can be reset.



API credentials are available securely for tests that require the live API, or suitable mocks/stubs are prepared.



Test cases and expected results have been reviewed before execution.



*Exit Criteria*



All planned test cases have a recorded status: Pass, Fail, Blocked, or Not Run.



All failed tests have a defect record or documented explanation.



All Critical and High severity defects are fixed and successfully retested, or formally recorded as accepted limitations.



Regression tests for changed areas have been executed.



Test summary, outstanding risks, and evidence links are complete.











