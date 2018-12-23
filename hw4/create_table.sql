-- write your table creation sql here!
CREATE TABLE create_table(
    id serial PRIMARY key,
    year INTEGER NOT NULL,
    month INTEGER NOT NULL,
    day INTEGER NOT NULL,
    country VARCHAR(50) NOT NULL,
    region VARCHAR(50) NOT NULL,
    city VARCHAR(50) NULL,
    multiple INTEGER NULL,
    success INTEGER NULL, 
    suicide INTEGER NULL, 
    no_kills INTEGER NULL
);