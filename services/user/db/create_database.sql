CREATE DATABASE IF NOT EXISTS users;
GO

USE users;
GO

CREATE TABLE IF NOT EXISTS user (
    id INT AUTO_INCREMENT PRIMARY KEY,
    full_name VARCHAR(100) NOT NULL,
    email VARCHAR(100) NOT NULL,
    phone_number INT NOT NULL,
    role_type INT NOT NULL,
    hashed_password VARCHAR(150) NOT NULL
);
