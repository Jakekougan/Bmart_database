
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
('Madeleine', 'Dartmouth', 'Iowa City', 'IO', '52240', '8616 Peter Drive', '444-000-9292', 'mdarty@gmail.com');

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




