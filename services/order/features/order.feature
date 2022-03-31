Feature: Handle Order submission

    Scenario Outline: The system can calculate the inventory
        Given a quantity <quantity>
        And a product id <product_id>
        When calculating the remaining inventory
        Then the result is <expected_result>
        Examples: Valid Order submission
            | quantity | product_id | expected_result |
            | 5        | 1          | 2               |

        Examples: Bad Order submission
            | quantity | product_id | expected_result |
            | 5        | 2          | -1              |
