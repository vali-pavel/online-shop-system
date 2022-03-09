Feature: Handle new Product creation and product retrieval

    Scenario Outline: A Merchant User can create products
        Given a user id <user_id>
        And product name <name>
        And product price <price>
        And product images <images>
        And product inventory <inventory>
        And product color <color>
        And product min delivery days <min_delivery_days>
        And product max_delivery_days <max_delivery_days>
        And product category <category>
        And sku <sku>
        And vendor name <vendor_name>
        When creating a new product
        Then Product fields validation <message>
        Examples: Good Product fields
            | user_id | name    | price | images         | inventory | color | min_delivery_days | max_delivery_days | category | sku           | vendor_name | message |
            | 1       | jeans   | 3.99  | IMAGE1, IMAGE2 | 10        | blue  | 2                 | 5                 | 0        | jeans-blue-1  | Vendor 1    | succeed |
            | 2       | t-shirt | 2.50  | IMAGE3         | 100       | blue  | 2                 | 5                 | 1        | tshirt-blue-1 | Vendor 2    | succeed |

        Examples: Bad Product fields
            | user_id | name         | price | images       | inventory | min_delivery_days | max_delivery_days | category | sku           | vendor_name | message                                                |
            | 1       | blue jeans   | 3.99  | PDF1, IMAGE2 | 10        | a                 | 5                 | a        | jeans-blue-1  | Vendor 1    | invalid files, invalid delivery days, invalid category |
            | 2       | blue t-shirt | 2.50a | TEXT1        | 100       | 2                 |                   | 1        | tshirt-blue-1 | Vendor 2    | invalid files, invalid price, missing delivery days    |

    Scenario Outline: The system returns a list of Products for Customer
        Given a pagination index <pagination_index>
        And a category <category>
        When customer views the Products
        Then I get a list of <total_products> Products
        And the list should have maximum '5' Products
        Examples:
            | pagination_index | category | total_products |
            | 0                |          | 5              |
            | 1                | 1        | 2              |
            | 1                | 2        | 5              |

    Scenario Outline: The system returns a list of Products for Merchant
        Given a user id <user_id>
        When merchant views his Products
        Then I get a list of <total_products> Products
        Examples:
            | user_id | total_products |
            | 1       | 10             |
            | 2       | 5              |
