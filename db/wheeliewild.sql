DROP TABLE IF EXISTS rentals;
DROP TABLE IF EXISTS vans;
DROP TABLE IF EXISTS customers;

CREATE TABLE customers (
    customer_name VARCHAR (255),
    license BOOLEAN,
    budget INT,
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
    start_date DATE,
    end_date DATE, 
    id SERIAL PRIMARY KEY
);

INSERT INTO customers (customer_name, license, budget, friends) VALUES ('Jenna', 'True', 1000, 4);
INSERT INTO customers (customer_name, license, budget, friends) VALUES ('Kirsten', 'True', 1000, 3);
INSERT INTO customers (customer_name, license, budget, friends) VALUES ('Rae', 'False', 500, 4);


INSERT INTO vans (van_name, reg_plate, year, capacity, type) VALUES ('Rocky', 'SN12 743','2012', 5, 'Luxury');
INSERT INTO vans (van_name, reg_plate, year, capacity, type) VALUES ('Steve', 'SN13 624','2013', 3, 'Luxury');
INSERT INTO vans (van_name, reg_plate, year, capacity, type) VALUES ('Roadster', 'SR18 766','2018', 2, 'Budget');
