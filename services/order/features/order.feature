Feature: Handle Order submission

    Scenario Outline: A Customer can submit an order
        Given customer id <customer_id>
        And order products <order_products>
        When the customer submits an Order
        Then customer data validation returns <customer_validation_status_code>
        And remaining inventory <remaining_inventory>
        And Order validation message <order_message>
        Examples: Valid Order submission
            | customer_id | order_products | customer_validation_status_code | remaining_inventory | order_message |
            | 1           | ORDER_PRODUCT1 | 200                             | 2                   | succeed       |
            | 2           | ORDER_PRODUCT2 | 200                             | 5                   | succeed       |

        Examples: Bad Order submission
            | customer_id | order_products | customer_validation_status_code | remaining_inventory | order_message              |
            | 3           | ORDER_PRODUCT1 | 422                             | 1                   | incomplete checkout data   |
            | 1000        | ORDER_PRODUCT2 | 404                             | 1                   | customer not found         |
            | 2           | ORDER_PRODUCT3 | 200                             | -200                | quantity exceeds inventory |
