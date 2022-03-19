DROP TABLE product;
DROP TABLE users;
DROP TABLE manufacturers;

CREATE TABLE users (
  id SERIAL PRIMARY KEY,
  name VARCHAR(255),
  type VARCHAR(255)
);

CREATE TABLE manufacturers (
  id SERIAL PRIMARY KEY,
  name VARCHAR(255),
  email VARCHAR(255),
  contact_number INT,
  manufacturer_type VARCHAR(255)
);

CREATE TABLE products (
  id SERIAL PRIMARY KEY,
  manufacturer_id INT REFERENCES manufacturers(id) ON DELETE CASCADE,
  name VARCHAR(255),
  type VARCHAR(255),
  cost INT,
  selling_price INT
);