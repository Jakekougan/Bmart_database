DROP TABLE IF EXISTS types;
CREATE TABLE types (
	type_name VARCHAR(30) PRIMARY KEY
);

DROP TABLE IF EXISTS vendor;
CREATE TABLE vendor (
	name VARCHAR(64)PRIMARY KEY
);

DROP TABLE IF EXISTS brands;
CREATE TABLE brands (
	brand_name VARCHAR(30) PRIMARY KEY,
	vendor_name VARCHAR(64) NOT NULL,
	FOREIGN KEY (vendor_name) REFERENCES vendor(name)
);

DROP TABLE IF EXISTS products;
CREATE TABLE bmart_products (
	upc CHAR(12) PRIMARY KEY,
	name VARCHAR(100) NOT NULL,
	weight DECIMAL(6,3) NOT NULL,
	volume DECIMAL(6,3) NOT NULL,
	quantity INTEGER NOT NULL,
	packaging VARCHAR(20),
	src_nation VARCHAR(50),
	hq_price DECIMAL(10, 2) NOT NULL,
    unit_price DECIMAL(10, 2) NOT NULL,
	brand_name VARCHAR(30),
	FOREIGN KEY (brand_name) REFERENCES brands(brand_name)
);

DROP TABLE IF EXISTS store;
CREATE TABLE store (
	store_num INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
	city VARCHAR(50) NOT NULL,
	state VARCHAR (15) NOT NULL,
	zip_code CHAR(5) NOT NULL CHECK(zip_code REGEXP '^[0-9]{5}$'),
	address VARCHAR (75) NOT NULL,
	phone_number CHAR(12) NOT NULL CHECK (phone_number REGEXP '^[0-9]{3}-[0-9]{3}-[0-9]{4}$'),
    UNIQUE (zip_code, address)
);

DROP TABLE IF EXISTS hrs_operating;
CREATE TABLE hrs_operating (
	store INT,
	FOREIGN KEY (store) REFERENCES store(store_num),
	day_of_week TINYINT NOT NULL CHECK (day_of_week BETWEEN 1 AND 7),
	PRIMARY KEY (store, day_of_week),
	opening_time TIME NOT NULL,
	closing_time TIME NOT NULL
);

DROP TABLE IF EXISTS shipment;
CREATE TABLE shipment (
	shipment_no INT AUTO_INCREMENT PRIMARY KEY,
	estimated_delivery TIMESTAMP NOT NULL,
	actual_arrival TIMESTAMP NOT NULL,
	delivered BOOLEAN NOT NULL,
    	store INT,
    	vendor VARCHAR(64),
	FOREIGN KEY (store) REFERENCES store(store_num),
	FOREIGN KEY (vendor) REFERENCES vendor(name)
);

DROP TABLE IF EXISTS reorder_requests;
CREATE TABLE reorder_requests(
	request_id INT AUTO_INCREMENT PRIMARY KEY,
	order_date TIMESTAMP NOT NULL,
	product CHAR(12),
	Product_qty INT NOT NULL,
	FOREIGN KEY (product) REFERENCES bmart_products(upc),
	store INT NOT NULL,
	FOREIGN KEY (store) REFERENCES store(store_num),
	cost	DECIMAL NOT NULL,
	viewed BOOLEAN NOT NULL,
    vendor VARCHAR(64),
    FOREIGN KEY (vendor) REFERENCES vendor(name),
	shipment_no INT,
	FOREIGN KEY (shipment_no) REFERENCES shipment(shipment_no)
    );
    

DROP TABLE IF EXISTS customers;
CREATE TABLE customers(
	customer_id INTEGER PRIMARY KEY AUTO_INCREMENT,
	first_name VARCHAR(100),
	last_name VARCHAR(100),
	city VARCHAR(50) NOT NULL,
	state VARCHAR (15) NOT NULL,
	zip_code CHAR(5) NOT NULL,
	address VARCHAR (75) NOT NULL,
	phone_number CHAR(12) NOT NULL, CHECK (phone_number REGEXP '^[0-9+-]+$'),
	email VARCHAR(255) NOT NULL UNIQUE, CHECK (email LIKE '%_@_%._%')
);

DROP TABLE IF EXISTS purchases;
CREATE TABLE purchases(
	purchase_id INT AUTO_INCREMENT PRIMARY KEY,
	purchase_date TIMESTAMP NOT NULL,
	price DECIMAL NOT NULL,
	online_order BOOLEAN,
	is_delivered BOOLEAN,
    	customer INT,
	FOREIGN KEY (customer) REFERENCES customers(customer_id)
);

DROP TABLE IF EXISTS order_items;
CREATE TABLE order_items (
	order_id INT, 
	product CHAR(12),
	quantity INT,
	PRIMARY KEY (order_id, product),
	FOREIGN KEY (order_id) REFERENCES purchases(purchase_id),
	FOREIGN KEY (product) REFERENCES bmart_products(upc)
);

DROP TABLE IF EXISTS inventory;
CREATE TABLE inventory (
	inventory_id INTEGER AUTO_INCREMENT PRIMARY KEY,
	product_num CHAR(12),
    	store INT,
	FOREIGN KEY (store) REFERENCES store(store_num),
	FOREIGN KEY (product_num) REFERENCES bmart_products(upc),
	max_amt INT NOT NULL,
	curr_amt INT NOT NULL,
	local_price DECIMAL NOT NULL,
	CONSTRAINT max_inventory CHECK(curr_amt <= max_amt)
);

DROP TABLE IF EXISTS product_types;
CREATE TABLE product_types (
	product CHAR(12),
	type VARCHAR(30),
	PRIMARY KEY (product, type),
	FOREIGN KEY (product) REFERENCES bmart_products(upc),
	FOREIGN KEY (type) REFERENCES types(type_name)
);
