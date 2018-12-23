CREATE TABLE avocado ( 
	avocado_id serial PRIMARY key,
    avocado_date DATE NOT NULL
);

CREATE TABLE price ( 
    price_id serial PRIMARY key,
    average_price FLOAT NOT NULL
);

CREATE TABLE avocado_price ( 
    avocado_id INTEGER REFERENCES avocado(avocado_id),
    price_id INTEGER REFERENCES price(price_id)
);

CREATE TABLE volume (
    volume_id serial PRIMARY key,
    total_volume FLOAT NOT NULL
);

CREATE TABLE avocado_volume ( 
    avocado_id INTEGER REFERENCES avocado(avocado_id),
    volume_id INTEGER REFERENCES volume(volume_id)

);

CREATE TABLE DATE ( 
    date_id serial PRIMARY key, 
    YEAR INTEGER NOT NULL
);

CREATE TABLE type (
    type_id serial PRIMARY key,
	type_name varchar(50) NOT NULL
);

CREATE TABLE region ( 
	region_id serial PRIMARY key, 
 	region_name varchar(50) NOT NULL
);
