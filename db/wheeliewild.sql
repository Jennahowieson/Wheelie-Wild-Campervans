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

INSERT INTO customers (customer_name, license, budget, friends) VALUES ('Jenna', 'True', 150, 2);
INSERT INTO customers (customer_name, license, budget, friends) VALUES ('Kirsten', 'True', 110, 2);
INSERT INTO customers (customer_name, license, budget, friends) VALUES ('Rae', 'True', 170, 2);
INSERT INTO customers (customer_name, license, budget, friends) VALUES ('Bruce', 'True', 50, 1);
INSERT INTO customers (customer_name, license, budget, friends) VALUES ('Connor', 'True', 70, 1);
INSERT INTO customers (customer_name, license, budget, friends) VALUES ('Tina', 'False', 200, 4);
INSERT INTO customers (customer_name, license, budget, friends) VALUES ('Stewart', 'True', 150, 3);
INSERT INTO customers (customer_name, license, budget, friends) VALUES ('Fran', 'False', 80, 2);
INSERT INTO customers (customer_name, license, budget, friends) VALUES ('Clare', 'True', 110, 3);
INSERT INTO customers (customer_name, license, budget, friends) VALUES ('Deb', 'False', 130, 1);





INSERT INTO vans (van_name, reg_plate, year, capacity, type) VALUES ('Rocky', 'BA47 B04','2022', 5, 'Luxury');
INSERT INTO vans (van_name, reg_plate, year, capacity, type) VALUES ('VanGogh', 'VI1N C3T','2021', 4, 'Luxury');
INSERT INTO vans (van_name, reg_plate, year, capacity, type) VALUES ('Vanny DeVito', 'DA4N N0Y','2018', 5, 'Budget');
INSERT INTO vans (van_name, reg_plate, year, capacity, type) VALUES ('Van Halen', 'GU17 A4R','2019', 3, 'Budget');
INSERT INTO vans (van_name, reg_plate, year, capacity, type) VALUES ('RV There Yet', 'DR11 V1N','2017', 4, 'Luxury');
INSERT INTO vans (van_name, reg_plate, year, capacity, type) VALUES ('Home Sweet Roam', 'HH00 M3E','2016', 3, 'Luxury');
INSERT INTO vans (van_name, reg_plate, year, capacity, type) VALUES ('Crewser', 'CR33 WSS','2020', 3, 'Budget');



INSERT INTO rentals (customer_id, van_id, start_date, end_date) VALUES (1, 1, '2022-12-23', '2022-12-26');
INSERT INTO rentals (customer_id, van_id, start_date, end_date) VALUES (2, 2, '2022-11-11', '2022-11-19');
INSERT INTO rentals (customer_id, van_id, start_date, end_date) VALUES (3, 3, '2022-12-02', '2022-12-05');
INSERT INTO rentals (customer_id, van_id, start_date, end_date) VALUES (4, 4, '2022-12-12', '2022-12-14');
INSERT INTO rentals (customer_id, van_id, start_date, end_date) VALUES (5, 5, '2022-11-13', '2022-11-26');
INSERT INTO rentals (customer_id, van_id, start_date, end_date) VALUES (6, 6, '2022-11-23', '2022-11-30');
INSERT INTO rentals (customer_id, van_id, start_date, end_date) VALUES (7, 7, '2022-11-15', '2022-11-30');
INSERT INTO rentals (customer_id, van_id, start_date, end_date) VALUES (8, 1, '2022-12-01', '2022-12-14');
