CREATE DATABASE IF NOT EXISTS products;
GO

USE products;
GO

CREATE TABLE IF NOT EXISTS product (
    id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT NOT NULL,
    name VARCHAR(50) NOT NULL,
    sku VARCHAR(50) NOT NULL,
    price FLOAT NOT NULL,
    color VARCHAR(50) NOT NULL,
    inventory INT NOT NULL,
    min_delivery_days INT NOT NULL,
    max_delivery_days INT NOT NULL,
    vendor_name VARCHAR(200) NOT NULL,
    category INT NOT NULL
);
