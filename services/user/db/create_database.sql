CREATE DATABASE IF NOT EXISTS users;
GO

USE users;
GO

CREATE TABLE IF NOT EXISTS user (
    user_id INT AUTO_INCREMENT PRIMARY KEY,
    full_name VARCHAR(100) NOT NULL,
    email VARCHAR(100) NOT NULL,
    phone_number INT NOT NULL,
    user_role INT NOT NULL,
    user_password VARCHAR(150) NOT NULL
);
