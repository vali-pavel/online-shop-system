Feature: Handle Auth operations

    Scenario Outline: The system can generate a valid JWT
        Given user id <user_id>
        And user role <user_role>
        When generating a jwt
        Then the fields validation message is <validation_message>
        And the jwt is <jwt>

        Examples: Good JWT is generated
            | user_id | user_role | secret_token | validation_message | jwt  |
            | 0       | 0         | secret123    | succeed            | JWT1 |
            | 1       | 1         | secret123    | succeed            | JWT2 |

        Examples: Bad JWT is generated
            | user_id | user_role | secret_token | validation_message | jwt      |
            | 3       | 0         | secret123    | fails              | BAD-JWT1 |

    Scenario Outline: The system can validate a JWT
        Given a jwt <jwt>
        When validating the jwt
        Then the status code is <status_code>

        Examples: Good JWT
            | jwt  | staus_code |
            | JWT1 | 200        |

        Examples: Bad JWT
            | jwt      | status_code |
            | BAD-JWT1 | 401         |
