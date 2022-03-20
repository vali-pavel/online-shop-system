Feature: Handle User login and new User creation

    Scenario Outline: The system can create a user
        Given email <email>
        And password <password>
        And full name <full_name>
        And phone number <phone_number>
        When creating a new user with the above details
        Then fields validation <result>
        Examples: Good Users
            | email                | password | full_name  | phone_number | result   |
            | john_doe@gmail.com   | pass123  | John Doe   | 0731352345   | succeeds |
            | john_smith@gmail.com | pass124  | John Smith | 0731352345   | succeeds |

        Examples: Bad Users
            | email                  | password | full_name | phone_number | result |
            | user_with_empty_fields | pass123  | John Doe  | 0731352345   | fails  |


    Scenario Outline: A user can Login
        Given a user with email <email>
        And a password <password>
        When the login button is clicked
        Then I should be redirected to the products page

        Examples: Good login fields
            | email                | password |
            | john_doe@gmail.com   | pass123  |
            | john_smith@gmail.com | pass124  |
