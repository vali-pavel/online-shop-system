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

    Scenario Outline: The system can create a user with Customer role
        Given a user with email <email>
        And password <password>
        And password <password>
        And full name <full_name>
        And phone number <phone_number>
        And role <role>
        When creating a new user with the above details
        Then User fields validation <result>
        Examples: Good Users
            | email                | password | full_name  | phone_number  | role | result   |
            | john_doe@gmail.com   | pass123  | John Doe   | 0040731352345 | 0    | succeeds |
            | john_smith@gmail.com | pass124  | John Smith | 0040731352345 | 1    | succeeds |

        Examples: Bad Users
            | email                            | password | full_name | phone_number  | role | result |
            | user_with_empty_fields@gmail.com |          | John Doe  |               |      | fails  |
            | user_with_invalid_role@gmail.com | pass124  | John Doe  | 0040731352345 | 99   | fails  |
            | user_with_invalid_email          | pass124  |           | 0040731352345 | 0    | fails  |
