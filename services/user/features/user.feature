Feature: Handle User login and new User creation

    Scenario: Login
        Given a login request
        When email is <email>
        And password is <password>
        Then I should get a <status_code> response

        Examples:
            | email              | password | status_code |
            | john_doe@gmail.com | pass123  | 200         |
            | test_1@gmail.com   | pass123  | 404         |
            |                    | pass123  | 422         |
            | test_1@gmail.com   |          | 422         |
