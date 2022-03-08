Feature: Handle new Customer creation, Customer data update and Checkout validation

    Scenario Outline: The system can create a Customer
        Given a user id <user_id>
        When creating a new Customer with the above user id
        Then I should get a <status_code> response

        Examples: Good customer creation fields
            | user_id | status_code |
            | 0       | 201         |
            | 1       | 201         |

        Examples: Bad customer creation fields
            | user_id | status_code |
            |         | 422         |
            | 1abc    | 422         |
            | 1000    | 404         |

    Scenario Outline: The system can update an existing Customer
        Given a customer id <customer_id>
        And a shipping address <shipping_address>
        And a billing address <billing_address>
        And a card number <card_number>
        And a card expiration <card_expiration>
        And a card holder <card_holder>
        When updating an existing customer with the above details
        Then I should get the <message> message and status code <status_code>
        Examples: Good customer fields
            | customer_id | shipping_address | billing_address | card_number         | card_expiration | card_holder | message | status_code |
            | 1           | New York         | New York        | 1111 2222 3333 4444 | 03/25           | John Doe    | succeed | 200         |
            | 2           | Craiova          | Craiova         | 1112 2222 3333 4444 | 02/24           | John Smith  | succeed | 200         |
        Examples: Bad customer fields
            | customer_id | shipping_address | billing_address | card_number         | card_expiration | card_holder | message                              | status_code |
            | 3           |                  |                 | 1111 2222 3333 4444 | 03/25           | John Doe 2  | invalid card holder                  | 422         |
            | 4           | Craiova          | Craiova         | 1112 2222 333 4444  | 02/2            | John Smith  | invalid card number, card expiration | 422         |
            | 1a          | Craiova          |                 |                     |                 |             | invalid customer id                  | 422         |

    Scenario Outline: The system should validate the Checkout information of a Customer
        Given a customer id <customer_id>
        When a checkout is submitted
        Then Customer fields validation <result>
        Examples: Customer has all fields
            | customer_id | result  |
            | 1           | succeed |
            | 2           | succeed |
        Examples: Customer is missing fields
            | customer_id | result |
            | 3           | fails  |
            | 4           | fails  |
