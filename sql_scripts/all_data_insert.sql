
INSERT into types VALUES ("Dairy");
INSERT into types VALUES ("Produce");
INSERT into types VALUES ("Meat");
INSERT into types VALUES ("Baked Goods");
INSERT into types VALUES ("Dry & Packaged Goods");
INSERT into types VALUES ("Beverages");
INSERT into types VALUES ("Health & Beauty");
INSERT into types VALUES ("Household Essentials");
INSERT into types VALUES ("Pet Supplies");
INSERT into types VALUES ("Alcohol");
INSERT into types VALUES ("Frozen Foods");
INSERT into types VALUES ("School/Office Supplies");
INSERT into types VALUES ("Clothing");
INSERT into types VALUES ("Sports Equipment");
INSERT into types VALUES ("Home Goods");

INSERT INTO vendor VALUES ("LibDib");
INSERT INTO vendor VALUES ("Pepsi Co");
INSERT INTO vendor VALUES ("Tyson Foods");
INSERT INTO vendor VALUES ("U.S Foods");
INSERT INTO vendor VALUES ("Coca-Cola");
INSERT INTO vendor VALUES ("Amazon Fresh");
INSERT INTO vendor VALUES ("Nestle");
INSERT INTO vendor VALUES ("General Mills");
INSERT INTO vendor VALUES ("Kraft Heinz");
INSERT INTO vendor VALUES ("Dole");
INSERT INTO vendor VALUES ("Chiquita");
INSERT INTO vendor VALUES ("Land O'Lakes");
INSERT INTO vendor VALUES ("Quaker Oats");
INSERT INTO vendor VALUES ("Fruit of the Loom");
INSERT INTO vendor VALUES ("Red Bull");
INSERT INTO vendor VALUES ("McCormick");
INSERT INTO vendor VALUES ("Clorox");
INSERT INTO vendor VALUES ("Glad");
INSERT INTO vendor VALUES ("Bounty");
INSERT INTO vendor VALUES ("Northern Tool");
INSERT INTO vendors (vendor_name) VALUES
('Heineken'),
('Budweiser'),
('Corona'),
('Guinness'),
('Stella Artois'),
('Beck''s'),
('Coors'),
('Pilsner Urquell'),
('Blue Moon'),
('Modelo'),
('Smirnoff'),
('Absolut'),
('Jack Daniel''s'),
('Jameson'),
('Captain Morgan'),
('Bacardi'),
('Johnnie Walker'),
('Chivas Regal'),
('Grey Goose'),
('Patrón'),
('Jose Cuervo'),
('Tanqueray'),
('Bombay'),
('Baileys Irish Cream'),
('Hennessy'),
('Disaronno'),
('Kahlúa'),
('Jägermeister'),
('Campari'),
('Aperol'),
('Sapporo'),
('Asahi'),
('Tsingtao'),
('Singha'),
('Red Stripe'),
('Carlsberg'),
('Tiger'),
('Molson'),
('Labatt'),
('Strongbow');

INSERT INTO brands (brand_name, vendor_name) VALUES
('Coca-Cola', 'Coca-Cola'),
('Red Bull', 'Red Bull'),
('Glad', 'Glad'),
('Tyson Foods', 'Tyson Foods'),
('Nestle', 'Nestle'),
('Quaker Oats', 'Quaker Oats'),
('Clorox', 'Clorox'),
('Fruit of the Loom', 'Fruit of the Loom'),
('General Mills', 'General Mills'),
('LibDib', 'LibDib'),
('Pepsi Co', 'Pepsi Co'),
('Amazon Fresh', 'Amazon Fresh'),
('McCormick', 'McCormick'),
('Chiquita', 'Chiquita'),
('U.S Foods', 'U.S Foods'),
('Kraft Heinz', 'Kraft Heinz'),
('Bounty', 'Bounty'),
('Dole', 'Dole'),
('Land O''Lakes', 'Land O''Lakes'),
('Heineken', 'Heineken'),
('Budweiser', 'Budweiser'),
('Corona', 'Corona'),
('Guinness', 'Guinness'),
('Stella Artois', 'Stella Artois'),
('Beck''s', 'Beck''s'),
('Coors', 'Coors'),
('Pilsner Urquell', 'Pilsner Urquell'),
('Blue Moon', 'Blue Moon'),
('Modelo', 'Modelo'),
('Smirnoff', 'Smirnoff'),
('Absolut', 'Absolut'),
('Jack Daniel''s', 'Jack Daniel''s'),
('Jameson', 'Jameson'),
('Captain Morgan', 'Captain Morgan'),
('Bacardi', 'Bacardi'),
('Johnnie Walker', 'Johnnie Walker'),
('Chivas', 'Chivas Regal'),
('Grey Goose', 'Grey Goose'),
('Patrón', 'Patrón'),
('Jose Cuervo', 'Jose Cuervo'),
('Tanqueray', 'Tanqueray'),
('Bombay', 'Bombay'),
('Baileys', 'Baileys Irish Cream'),
('Hennessy', 'Hennessy'),
('Disaronno', 'Disaronno'),
('Kahlúa', 'Kahlúa'),
('Jägermeister', 'Jägermeister'),
('Campari', 'Campari'),
('Aperol', 'Aperol'),
('Sapporo', 'Sapporo'),
('Asahi', 'Asahi'),
('Tsingtao', 'Tsingtao'),
('Singha', 'Singha'),
('Red Stripe', 'Red Stripe'),
('Carlsberg', 'Carlsberg'),
('Tiger', 'Tiger'),
('Molson', 'Molson'),
('Labatt', 'Labatt'),
('Strongbow', 'Strongbow');


INSERT INTO customers (first_name, last_name, city, state, zip_code, address, phone_number, email) VALUES
('John', 'Doe', 'Springfield', 'IL', '62704', '123 Elm Street', '217-555-1234', 'jdoe@iwu.edu'),
('Jane', 'Smith', 'Chicago', 'IL', '60614', '456 Oak Avenue', '312-555-5678', 'janesmith@yahoo.com'),
('Robert', 'Brown', 'Peoria', 'IL', '61602', '789 Maple Lane', '309-555-9876', 'robbrown@gmail.com'),
('Emily', 'Johnson', 'Rockford', 'IL', '61101', '234 Birch Drive', '815-555-6543', 'emjohnson@outlook.com'),
('Michael', 'Taylor', 'Normal', 'IL', '61761', '567 Pine Road', '309-555-4321', 'michaeltaylor@gmail.com'),
('Sophia', 'Williams', 'Decatur', 'IL', '62522', '891 Cedar Blvd', '217-555-7890', 'sophiawilliams@jesus.com'),
('Jacob', 'Martinez', 'Bloomington', 'IL', '61701', '112 Walnut Circle', '309-555-5670', 'jacob.martinez@egmail.com'),
('Olivia', 'Davis', 'Champaign', 'IL', '61820', '334 Willow Path', '217-555-3456', 'olivia.davis@gmail.com'),
('William', 'Garcia', 'Naperville', 'IL', '60540', '778 Chestnut Terrace', '630-555-1230', 'william.garcia@gmail.com'),
('Emma', 'Lopez', 'Aurora', 'IL', '60504', '990 Fir Court', '630-555-6789', 'emma.lopez@yahoo.com'),
('Jake', 'Kougan', 'Frankfort', 'IL', '60423', '8616 Huckins Drive', '312-718-1065', 'jakekougan6@gmail.com'),
('Jalynn', 'Ford', 'LeRoy', 'IL', '61752', '111 Kite Court', '618-830-7929', 'jfo@gmail.com'),
('Bruce', 'Wayne', 'Gotham City', 'NJ', '08001', '1007 Mountain Drive', '215-919-1939', 'bwayne6@gwaynetech.com'),
('Peter', 'Parker', 'Queens', 'NY', '07831', '20 Ingram Street', '718-815-1963', 'pparker@esu.edu'),
('Issac', 'Clarke', 'Denver', 'CO', '80203', '3616 Winnetka Rd', '954-244-2008', 'issacclarke@ishimaura.com'),
('Daffy', 'Duck', 'Los Angeles', 'CA', '90001', '1673 Bibo Drive', '123-456-7890', 'dduck@gmail.com'),
('Alex', 'Mason', 'Fairbanks', 'AL', '99703', '2010 Kino Street', '867-992-1011', 'alexmas@cia.gov'),
('Tony', 'Stank', 'Malibu', 'CA', '90263', '1637 Walker Drive', "111-222-3333", 'stanky@gmail.com'),
('Benny', 'Ballgame', 'Orlando', 'FL', '32789', '1214 Noway Road', '899-234-5765', 'bennyandthejets@gmail.com'),
('Johnny', 'Test', 'Seattle', 'WA', '98039', '212 Main Street', '102-602-4545', 'crimelordfr@gmail.com'),
('Randy', 'Orton', 'St Louis', 'MO', '63101', '123 Winner Road', '619-355-0000', 'ottanowhere@gmail.com'),
('Kendra', 'Daniels', 'Boston', 'MA', '02108', '1221 Kellion Drive', '444-555-9999', 'kdaniels@ishimaura.com'),
('Kayla', 'Halawa', 'Minneapolis', 'MN', '55401', '2 Night Street', '617-716-0000', 'dartyparty6@gmail.com'),
('Jake', 'Miller', 'Peoria', 'IL', '61604', '1025 Oakwood Dr', '3095554321', 'jake.miller@example.com'),
("Liam", "Smith", "Chicago", "Illinois", "60616", "1310 S State St", "312-555-0101", "lsmith@gmail.com"),
("Noah", "Johnson", "Brooklyn", "New York", "11201", "45 Court St", "718-819-0122", "njohnson2@gmail.com"),
("Oliver", "Brown", "Los Angeles", "California", "90017", "850 S Grand Ave", "213-855-0189", "obrown@gmail.com"),
("Henry", "Jones", "Phoenix", "Arizona", "85004", "101 N 1st Ave", "602-910-3819", "hjones@gmail.com"),
("Lukas", "Garcia", "Miami", "Florida", "33130", "234 SW 8th St", "305-824-2941", "lgarcia@gmail.com"),
("Benjamin", "Ramirez", "San Diego", "California", "92101", "600 W Broadway", "619-293-9422", "bramirez@gmail.com"),
("Owen", "Miller", "Boston", "Massachusetts", "02108", "1 Beacon St", "617-249-0123", "omiller@gmail.com"),
("Jackson", "Rodriguez", "Seattle", "Washington", "98101", "1420 5th Ave", "206-111-4012", "jramirez@gmail.com"),
("Gabriel", "Martinez", "Minneapolis", "Minnesota", "55402", "90 S 7th St", "612-999-1000", "gmartinez@gmail.com"),
("Isabella", "Hernandez", "Denver", "Colorado", "80202", "999 18th St", "720-300-9100", "ihernndez@gmail.com"),
("Elizabeth", "Thomas", "Little Rock", "Arkansas", "72201", "400 W Capitol Ave", "501-091-9481", "miataylor@gmail.com"),
("Mia", "Taylor", "Houston", "Texas", "77002", "1001 McKinney St", "713-218-9021", "mtaylor@gmail.com"),
("Ava", "Moore", "Washington", "DC", "20002", "400 Massachusetts Ave NE", "202-498-9351", "avamoore@gmail.com"),
("Evelyn", "Lee", "Philadelphia", "Pennsylvania", "19107", "1234 Market St", "215-349-9521", "elee@gmail.com"),
("Cench", "Cee", "Atlanta", "Georgia", "30303", "200 Peachtree St NW", "404-525-9481", "cenchcee@gmail.com");


INSERT INTO store (city, state, zip_code, address, phone_number) VALUES
('New York City', 'NY', '10001', '1234 Elm Street', '212-555-1234'),
('Los Angeles', 'CA', '90001', '5678 Sunset Boulevard', '323-555-5678'),
('Chicago', 'IL', '60601', '9101 Michigan Avenue', '312-555-9101'),
('Houston', 'TX', '77002', '1122 Main Street', '713-555-1122'),
('Phoenix', 'AZ', '85001', '3344 Camelback Road', '602-555-3344'),
('Philadelphia', 'PA', '19102', '5566 Market Street', '215-555-5566'),
('San Antonio', 'TX', '78209', '7788 Broadway Street', '210-555-7788'),
('San Diego', 'CA', '92101', '9900 Pacific Highway', '619-555-9900'),
('Dallas', 'TX', '75201', '2233 Elm Street', '214-555-2233'),
('San Jose', 'CA', '95110', '4455 Santa Clara Street', '408-555-4455'),
('Austin', 'TX', '78701', '6677 Lamar Boulevard', '512-555-6677'),
('Jacksonville', 'FL', '32246', '8899 Beach Boulevard', '904-555-8899'),
('Fort Worth', 'TX', '76102', '1001 Main Street', '817-555-1001'),
('Columbus', 'OH', '43210', '1122 High Street', '614-555-1122'),
('Charlotte', 'NC', '28205', '3344 Tryon Street', '704-555-3344'),
('San Francisco', 'CA', '94102', '5566 Market Street', '415-555-5566'),
('Indianapolis', 'IN', '46204', '7788 Meridian Street', '317-555-7788'),
('Seattle', 'WA', '98104', '9900 1st Avenue', '206-555-9900'),
('Denver', 'CO', '80206', '2233 Colfax Avenue', '303-555-2233'),
('Washington', 'DC', '20001', '4455 Constitution Avenue', '202-555-4455'),
('Nashville', 'TN', '37203', '6677 Broadway', '615-555-6677'),
('Oklahoma City', 'OK', '73102', '8899 Broadway Avenue', '405-555-8899'),
('Boston', 'MA', '02215', '1001 Beacon Street', '617-555-1001'),
('El Paso', 'TX', '79901', '2345 Montana Avenue', '915-555-2345'),
('Portland', 'OR', '97209', '4567 Burnside Street', '503-555-4567'),
('Las Vegas', 'NV', '89101', '6789 Fremont Street', '702-555-6789'),
('Detroit', 'MI', '48226', '1357 Woodward Avenue', '313-555-1357'),
('Memphis', 'TN', '38103', '2468 Beale Street', '901-555-2468'),
('Louisville', 'KY', '40205', '3690 Bardstown Road', '502-555-3690'),
('Baltimore', 'MD', '21201', '1478 Pratt Street', '410-555-1478'),
('Milwaukee', 'WI', '53202', '2580 Wisconsin Avenue', '414-555-2580'),
('Albuquerque', 'NM', '87106', '3691 Central Avenue', '505-555-3691'),
('Tucson', 'AZ', '85710', '7412 Broadway Blvd', '520-555-7412'),
('Fresno', 'CA', '93710', '9630 Blackstone Avenue', '559-555-9630'),
('Sacramento', 'CA', '95814', '8524 Capitol Mall', '916-555-8524'),
('Mesa', 'AZ', '85201', '7531 Main Street', '480-555-7531'),
('Kansas City', 'MO', '64108', '1597 Grand Blvd', '816-555-1597'),
('Atlanta', 'GA', '30303', '9513 Peachtree Street', '404-555-9513'),
('Miami', 'FL', '33137', '6420 Biscayne Blvd', '305-555-6420'),
('Raleigh', 'NC', '27607', '3141 Hillsborough Street', '919-555-3141');


INSERT INTO bmart_products VALUES
('100000000001', 'Coca-Cola Can 12pk', 0.5, 0.33, 12, 'Cans', 'USA', 6.99, 4.99, 'Coca-Cola'),
('100000000002', 'Red Bull 4pk', 0.3, 0.25, 4, 'Cans', 'Austria', 8.99, 5.99, 'Red Bull'),
('100000000003', 'Glad Trash Bags', 1.2, 0.80, 40, 'Box', 'USA', 9.49, 6.99, 'Glad'),
('100000000004', 'Tyson Chicken Nuggets', 0.9, 0.50, 1, 'Bag', 'USA', 7.99, 4.99, 'Tyson Foods'),
('100000000005', 'Nestlé Chocolate Bar', 0.2, 0.10, 1, 'Wrapper', 'Switzerland', 1.99, 0.99, 'Nestlé'),
('100000000006', 'Quaker Oats Canister', 1.0, 0.70, 1, 'Canister', 'USA', 4.99, 2.29, 'Quaker Oats'),
('100000000007', 'Clorox Wipes', 0.7, 0.50, 1, 'Canister', 'USA', 5.49, 3.29, 'Clorox'),
('100000000008', 'Fruit of the Loom Socks 6pk', 0.6, 0.30, 6, 'Plastic', 'USA', 10.99, 7.99, 'Fruit of the Loom'),
('100000000009', 'General Mills Cereal', 0.8, 0.60, 1, 'Box', 'USA', 3.99, 2.79, 'General Mills'),
('100000000010', 'LibDib Wine Bottle', 1.1, 0.75, 1, 'Glass', 'France', 12.99, 8.99, 'LibDib'),

('100000000011', 'Pepsi 6pk Bottles', 0.5, 0.50, 6, 'Plastic', 'USA', 5.99, 3.69, 'Pepsi Co'),
('100000000012', 'Amazon Fresh Bananas', 1.2, 0.30, 6, 'Bundle', 'Ecuador', 1.49, 0.99, 'Amazon Fresh'),
('100000000013', 'McCormick Black Pepper', 0.1, 0.10, 1, 'Jar', 'USA', 3.49, 2.19, 'McCormick'),
('100000000014', 'Chiquita Plantains', 1.1, 0.40, 3, 'Bundle', 'Honduras', 1.79, 0.69, 'Chiquita'),
('100000000015', 'U.S. Foods Ground Beef', 1.0, 0.70, 1, 'Wrap', 'USA', 6.49, 4.29, 'U.S. Foods'),
('100000000016', 'Kraft Heinz Mac & Cheese', 0.5, 0.50, 1, 'Box', 'USA', 2.99, 1.79, 'Kraft Heinz'),
('100000000017', 'Nestlé Water 24pk', 0.6, 0.50, 24, 'Plastic', 'USA', 4.49, 2.29, 'Nestlé'),
('100000000018', 'Bounty Paper Towels', 0.9, 0.80, 6, 'Rolls', 'USA', 10.99, 7.49, 'Bounty'),
('100000000019', 'Dole Pineapple Chunks', 0.3, 0.30, 1, 'Can', 'Philippines', 2.19, 1.09, 'Dole'),
('100000000020', 'Land O''Lakes Butter', 0.5, 0.50, 1, 'Box', 'USA', 3.59, 2.39, 'Land O''Lakes'),

('100000000021', 'Coca-Cola Mini Cans 6pk', 0.4, 0.22, 6, 'Cans', 'USA', 4.49, 3.39, 'Coca-Cola'),
('100000000022', 'Pepsi Max 12pk', 0.5, 0.33, 12, 'Cans', 'USA', 6.99, 4.79, 'Pepsi Co'),
('100000000023', 'Red Bull Sugar Free 4pk', 0.3, 0.25, 4, 'Cans', 'Austria', 9.49, 6.59, 'Red Bull'),
('100000000024', 'Fruit of the Loom T-Shirts', 0.8, 0.20, 3, 'Bag', 'USA', 14.99, 10.49, 'Fruit of the Loom'),
('100000000025', 'McCormick Cinnamon', 0.1, 0.10, 1, 'Jar', 'USA', 2.99, 1.69, 'McCormick'),
('100000000026', 'Glad Freezer Bags 20ct', 0.4, 0.40, 20, 'Box', 'USA', 3.99, 2.79, 'Glad'),
('100000000027', 'Tyson Grilled Chicken', 0.9, 0.60, 1, 'Bag', 'USA', 7.49, 5.49, 'Tyson Foods'),
('100000000028', 'General Mills Granola Bars', 0.5, 0.40, 6, 'Box', 'USA', 4.29, 3.39, 'General Mills'),
('100000000029', 'Amazon Fresh Spinach', 0.3, 0.30, 1, 'Bag', 'USA', 2.99, 1.59, 'Amazon Fresh'),
('100000000030', 'Chiquita Bananas', 1.0, 0.40, 6, 'Bundle', 'Guatemala', 1.39, 0.79, 'Chiquita'),

('100000000031', 'Nestlé Coffee Creamer', 0.6, 0.50, 1, 'Bottle', 'USA', 3.99, 2.59, 'Nestlé'),
('100000000032', 'Kraft Heinz Ketchup', 0.9, 0.70, 1, 'Bottle', 'USA', 2.99, 1.59, 'Kraft Heinz'),
('100000000033', 'Dole Salad Mix', 0.5, 0.30, 1, 'Bag', 'USA', 2.49, 1.29, 'Dole'),
('100000000034', 'Clorox Bleach', 1.2, 0.90, 1, 'Bottle', 'USA', 4.79, 3.59, 'Clorox'),
('100000000035', 'LibDib Red Wine', 1.3, 0.75, 1, 'Glass', 'Italy', 14.99, 7.99, 'LibDib'),
('100000000036', 'Quaker Oats Overnight Cups', 0.4, 0.30, 1, 'Cup', 'USA', 2.49, 1.29, 'Quaker Oats'),
('100000000037', 'Land O''Lakes Cheese Slices', 0.5, 0.50, 1, 'Pack', 'USA', 3.89, 2.49, 'Land O''Lakes'),
('100000000038', 'Nestlé Ice Cream Pint', 0.8, 0.80, 1, 'Tub', 'USA', 4.99, 2.99, 'Nestlé'),
('100000000039', 'U.S. Foods Bacon', 0.7, 0.50, 1, 'Wrap', 'USA', 5.99, 2.99, 'U.S. Foods'),
('100000000040', 'Pepsi Co Lip Balm Pack', 0.1, 0.10, 3, 'Blister', 'USA', 3.49, 2.29, 'Pepsi Co'),

('100000000041', 'McCormick Taco Seasoning', 0.1, 0.10, 1, 'Packet', 'USA', 0.99, 0.49, 'McCormick'),
('100000000042', 'Red Bull Yellow Edition 4pk', 0.3, 0.25, 4, 'Cans', 'Austria', 9.99, 7.59, 'Red Bull'),
('100000000043', 'Clorox Toilet Cleaner', 0.9, 0.80, 1, 'Bottle', 'USA', 3.49, 2.19, 'Clorox'),
('100000000044', 'Glad Sandwich Bags 100ct', 0.4, 0.50, 100, 'Box', 'USA', 5.49, 3.29, 'Glad'),
('100000000045', 'Coca-Cola Glass Bottle 6pk', 1.0, 0.33, 6, 'Glass', 'Mexico', 7.99, 6.99, 'Coca-Cola'),
('100000000046', 'Tyson Chicken Strips', 0.9, 0.60, 1, 'Bag', 'USA', 8.99, 7.49, 'Tyson Foods'),
('100000000047', 'General Mills Cookie Mix', 0.6, 0.50, 1, 'Box', 'USA', 3.79, 2.89, 'General Mills'),
('100000000048', 'Quaker Rice Cakes', 0.5, 0.40, 1, 'Bag', 'USA', 3.29, 2.09, 'Quaker Oats'),
('100000000049', 'Dole Fruit Bowls 4pk', 0.3, 0.40, 4, 'Cups', 'USA', 2.99, 1.79, 'Dole'),
('100000000050', 'Fruit of the Loom Hoodie', 1.5, 0.90, 1, 'Bag', 'USA', 24.99, 21.99, 'Fruit of the Loom');
DELETE FROM bmart_products;



INSERT INTO inventory (product_num, store, max_amt, curr_amt, local_price) VALUES
('100000000001', 1, 100, 60, 7.49),
('100000000002', 1, 80, 50, 9.49),
('100000000003', 1, 60, 30, 9.99),

('100000000004', 2, 40, 15, 8.29),
('100000000005', 2, 120, 100, 2.49),
('100000000006', 2, 90, 60, 5.25),

('100000000007', 3, 75, 40, 5.75),
('100000000008', 3, 55, 40, 10.99),
('100000000009', 3, 85, 65, 4.39),

('100000000010', 4, 35, 20, 13.49),
('100000000011', 4, 100, 80, 6.25),
('100000000012', 4, 150, 100, 1.25),

('100000000013', 5, 40, 20, 3.79),
('100000000014', 5, 50, 25, 1.99),
('100000000015', 5, 70, 40, 6.75),

('100000000016', 6, 90, 70, 3.49),
('100000000017', 6, 60, 35, 4.69),
('100000000018', 6, 45, 30, 11.99),

('100000000019', 7, 50, 25, 2.29),
('100000000020', 7, 80, 50, 3.99),
('100000000021', 7, 100, 65, 4.69),

('100000000022', 8, 80, 45, 7.25),
('100000000023', 8, 75, 40, 9.99),
('100000000024', 8, 60, 35, 14.99),

('100000000025', 9, 55, 40, 3.09),
('100000000026', 9, 90, 60, 4.59),
('100000000027', 9, 70, 30, 8.25),

('100000000028', 10, 100, 80, 4.49),
('100000000029', 10, 50, 30, 3.25),
('100000000030', 10, 85, 50, 1.39),

('100000000031', 11, 45, 30, 3.79),
('100000000032', 11, 55, 40, 3.39),
('100000000033', 11, 50, 30, 2.49),

('100000000034', 12, 60, 35, 4.99),
('100000000035', 12, 40, 20, 14.99),
('100000000036', 12, 70, 40, 2.79),

('100000000037', 13, 60, 30, 3.75),
('100000000038', 13, 80, 55, 5.25),
('100000000039', 13, 50, 25, 6.25),

('100000000040', 14, 90, 60, 3.49),
('100000000041', 14, 120, 100, 1.09),
('100000000042', 14, 60, 30, 10.25),

('100000000043', 15, 55, 40, 3.79),
('100000000044', 15, 80, 60, 6.25),
('100000000045', 15, 65, 35, 8.99),

('100000000046', 16, 70, 30, 9.49),
('100000000047', 16, 75, 45, 3.89),
('100000000048', 16, 50, 35, 3.49),

('100000000049', 17, 60, 40, 2.79),
('100000000050', 17, 40, 25, 25.99);