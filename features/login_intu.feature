Feature: Intu login
    Scenario: Successful intu login
        Given the user is in the intu login page
        When the user logs in with valid intu credentials
        Then user should be redirected to dashboard page