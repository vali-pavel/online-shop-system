CREATE DATABASE IF NOT EXISTS customers;
GO

USE customers;
GO

CREATE TABLE IF NOT EXISTS customer (
    id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT NOT NULL,
    shipping_address VARCHAR(250),
    billing_address VARCHAR(250),
    card_number INT,
    card_expiration DATE,
    card_holder VARCHAR(100)
);
