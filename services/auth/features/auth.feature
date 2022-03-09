Feature: Handle Auth operations

    Scenario Outline: The system can generate a valid authentication token
        Given user id <user_id>
        And user role <user_role>
        When generating an auth token
        Then the fields validation message is <validation_message>
        And the auth token is <auth_token>

        Examples: Good auth token is generated
            | user_id | user_role | secret_token | validation_message | auth_token  |
            | 0       | 0         | secret123    | succeed            | AUTH-TOKEN1 |
            | 1       | 1         | secret123    | succeed            | AUTH-TOKEN2 |

        Examples: Bad auth token is generated
            | user_id | user_role | secret_token | validation_message | auth_token      |
            | 3       | 0         | secret123    | fails              | BAD-AUTH-TOKEN1 |

    Scenario Outline: The system can validate an authentication token
        Given an auth token <auth_token>
        When validating the auth token
        Then the status code is <status_code>

        Examples: Good auth token
            | auth_token  | staus_code |
            | AUTH-TOKEN1 | 200        |

        Examples: Bad auth token
            | auth_token      | status_code |
            | BAD-AUTH-TOKEN1 | 401         |
