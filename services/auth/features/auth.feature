Feature: Handle Auth operations

    Scenario Outline: The system can generate a valid authentication token
        Given user id <user_id>
        And user role <user_role>
        And secret key <secret_key>
        When generating an auth token
        Then the auth token is <auth_token>

        Examples: Good auth token is generated
            | user_id | user_role | secret_key | auth_token  |
            | 0       | 0         | secret123  | AUTH-TOKEN1 |
            | 1       | 1         | secret123  | AUTH-TOKEN2 |

        Examples: Bad auth token is generated
            | user_id | user_role | secret_key     | auth_token      |
            | 3       | 0         | invalid-secret | BAD-AUTH-TOKEN1 |

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
