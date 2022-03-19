-- DROP TABLE product;
-- DROP TABLE users;
-- DROP TABLE manufacturers;

-- CREATE TABLE users (
--   id SERIAL PRIMARY KEY,
--   name VARCHAR(255),
--   category VARCHAR(255)
-- );

-- CREATE TABLE manufacturers (
--   id SERIAL PRIMARY KEY,
--   name VARCHAR(255),
--   email VARCHAR(255),
--   contact_number INT,
--   category VARCHAR(255)
-- );

-- CREATE TABLE products (
--   id SERIAL PRIMARY KEY,
--   manufacturer_id INT REFERENCES manufacturers(id) ON DELETE CASCADE,
--   name VARCHAR(255),
--   category VARCHAR(255),
--   cost INT,
--   selling_price INT
-- );

-- INSERT INTO users (name, category) VALUES ('Papi' , 'Shop Manager');
-- INSERT INTO manufacturers (name, email, contact_number, category) VALUES ('jose', 'jose@aa.com', '1234', 'Accesories');
-- INSERT INTO products (name, category, cost, selling_price) VALUES ('Thermometer' , 'Accesories', 2, 4);

-- SELECT * FROM users;
-- SELECT * FROM manufacturers;
-- SELECT * FROM products;
