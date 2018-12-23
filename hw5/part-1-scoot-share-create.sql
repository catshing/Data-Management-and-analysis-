part-1-scoot-share-create.sql

CREATE TABLE CustomerInfo (
  customer_id SERIAL PRIMARY KEY,
  firstName VARCHAR(50) NOT NULL,
  lastName VARCHAR(50) NOT NULL,
  TimeEntered DATE NOT NULL DEFAULT CURRENT_DATE,
  email VARCHAR(200) NOT NULL, 
  streetName VARCHAR(100) NOT NULL,
  streetName VARCHAR(100) NOT NULL,
  city VARCHAR(50) NOT NULL,
  state VARCHAR(50) NOT NULL,
  zipCode VARCHAR(20) NOT NULL,
  cellphone VARCHAR(100) NOT NULL
);

CREATE TABLE CustomerReferredBy (
  referred_id SERIAL PRIMARY KEY,
  customer_id INTEGER REFERENCES CustomerInfo (customer_id),
  firstName VARCHAR(50) NOT NULL,
  lastName VARCHAR(50) NOT NULL
);

CREATE TABLE ScooterInfo (
  scooter_id serial PRIMARY KEY,
  rangeInkm NUMERIC(5,2) NOT NULL,
  weightInkm NUMERIC(5,2) NOT NULL,
  topSpeed_kmhr NUMERIC(5,2) NOT NULL,
  condition VARCHAR(50) NOT NULL,
  manufacturerCountry VARCHAR(50) NOT NULL,
  manufacturer VARCHAR(50) NOT NULL,
  modelNumber VARCHAR(50) NOT NULL,
  available VARCHAR(50) NOT NULL
);

CREATE TABLE BorrowInfo (
  borrow_id serial PRIMARY KEY,
  customer_id INTEGER REFERENCES CustomerInfo (customer_id),
  scooter_id  INTEGER REFERENCES ScooterInfo (scooter_id)
  timeBorrowed DATE NOT NULL DEFAULT CURRENT_DATE,
  timeNeedReturn DATE NOT NULL,
  numHours INTEGER NOT NULL,
  amountPaid NUMERIC(5,2) NOT NULL
);

CREATE TABLE ScooterReturn (
  scooterReturned_id serial PRIMARY KEY,
  scooter_id INTEGER REFERENCES ScooterInfo (scooter_id),
  timeReturned DATE NOT NULL DEFAULT CURRENT_DATE,
  isLate VARCHAR(20) NOT NULL,
  hasDamages VARCHAR(20) NOT NULL,
  flag VARCHAR(20) NOT NULL,
  lateDamageFees INTEGER NULL
);

CREATE TABLE ScooterNotes (
  notes_id SERIAL PRIMARY KEY,
  borrowed_id INTEGER REFERENCES BorrowInfo (borrow_id),
  Issues VARCHAR(500) NOT NULL,
  category VARCHAR(500) NOT NULL
);