CREATE DATABASE IF NOT EXISTS sarias_river;

USE sarias_river;

CREATE TABLE IF NOT EXISTS reservations (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100),
    email VARCHAR(100),
    suite VARCHAR(100),
    date VARCHAR(20)
);
