DROP TABLE IF EXISTS rentals;
DROP TABLE IF EXISTS vans;
DROP TABLE IF EXISTS customers;

CREATE TABLE customers (
    customer_name VARCHAR (255),
    license BOOLEAN,
    budget VARCHAR (255),
    friends INT,
    id SERIAL PRIMARY KEY
);

CREATE TABLE vans(
    van_name VARCHAR (255),
    reg_plate VARCHAR (255),
    year INT,
    capacity INT,
    type VARCHAR(255),
    id SERIAL PRIMARY KEY
);

CREATE TABLE rentals(
    customer_id INT REFERENCES customers(id),
    van_id INT REFERENCES vans(id),
    rental_duration INT, 
    id SERIAL PRIMARY KEY
);

INSERT INTO customers (customer_name, license, budget, friends) VALUES ('Jenna', 'True', 1000, 4);

INSERT INTO vans (van_name, reg_plate, year, capacity, type) VALUES ('Rocky', 'SN12 743',2012, 5, 'Luxury');
INSERT INTO vans (van_name, reg_plate, year, capacity, type) VALUES ('Steve', 'SN13 624',2013, 5, 'Luxury');
INSERT INTO vans (van_name, reg_plate, year, capacity, type) VALUES ('Roadster', 'SR18 766',2018, 5, 'Budget');

INSERT INTO rentals (customer_id, van_id, rental_duration) VALUES (1,1,4)