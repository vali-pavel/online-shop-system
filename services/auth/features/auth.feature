Feature: Handle Auth operations

    Scenario Outline: The system can generate a valid authentication token
        Given user id <user_id>
        And user role <user_role>
        And secret key <secret_key>
        When generating an auth token
        Then the auth token is <auth_token>

        Examples: Good auth token is generated
            | user_id | user_role | secret_key          | auth_token  |
            | 0       | 0         | Strong_Secret_Key1! | AUTH-TOKEN1 |
            | 1       | 1         | Strong_Secret_Key1! | AUTH-TOKEN2 |

        Examples: Bad auth token is generated
            | user_id | user_role | secret_key     | auth_token      |
            | 3       | 0         | invalid-secret | BAD-AUTH-TOKEN1 |

    Scenario Outline: The system can validate an authentication token
        Given an auth token <auth_token>
        When validating the auth token
        Then valid token <is_token_valid>

        Examples: Good auth token
            | auth_token  | is_token_valid |
            | AUTH-TOKEN1 | True           |

        Examples: Bad auth token
            | auth_token      | is_token_valid |
            | BAD-AUTH-TOKEN1 | False          |
