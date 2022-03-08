Feature: Handle User login and new User creation

    Scenario Outline: A user can Login
        Given an user with email <email>
        And password <password>
        When logging in to the application
        Then I should get a <status_code> response

        Examples: Good login fields
            | email                | password | status_code |
            | john_doe@gmail.com   | pass123  | 200         |
            | john_smith@gmail.com | pass123  | 201         |

        Examples: Bad login fields
            | email            | password | status_code |
            | test_1@gmail.com | pass123  | 404         |
            |                  | pass123  | 422         |
            | test_1@gmail.com |          | 422         |
