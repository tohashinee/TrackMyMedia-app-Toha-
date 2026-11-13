**Test Summary Report — TrackMyMedia (Test Cycle 1)**



• Project Name: TrackMyMedia CLI Application (v1.0)

• Test Author: Tohashinee Manohur

• Test Environment: Python 3.14.3, unittest Framework, SQLite3, Windows OS



*1. Executive Summary*



Cycle 1 testing was executed against the baseline v1.0 build to verify Functional Requirements (FR-01–FR-05) and Non-Functional Requirements (NFR-01–NFR-04). Core database CRUD operations and SQL injection protections passed, while 1 runtime defect (DEF-01) was identified and logged for remediation.



*2. Cycle 1 Execution Metrics*



• Total Planned Test Cases: 8 (TC-01 through TC-08)

• Passed: 7 (87.5%)

• Failed: 1 (12.5%) — TC-07 (DEF-01: Unhandled network timeout)

• Blocked / Not Run: 0 (0%)

• Total Defects Logged: 1 (High)



*3. Exit Criteria Assessment \& Release Decisio*n



Exit Criterion (from Test Plan)	                                 Status	                Assessment Notes

All planned test cases have a recorded status.	                  Met	     8/8 test cases executed with terminal and automated evidence.

All failed tests have a documented defect record.	          Met	     TC-07 failure mapped to DEF-01 with stack trace evidence.

All Critical and High severity defects are fixed and retested.	 Not Met     DEF-01 (High) remains open, awaiting code remediation.

Regression tests for changed areas have been executed.	         Pending     Scheduled for Cycle 2 once DEF-01 fix is delivered.



• Release Recommendation: DO NOT RELEASE (Conditional Hold)

• Next Steps: Hand over DEF-01 (High) to development for remediation, followed by Cycle 2 regression testing before production sign-off.



