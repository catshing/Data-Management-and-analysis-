CREATE TABLE staging_avocado ( 
    avocado_id serial PRIMARY KEY,
    avocado_date DATE NOT null,
    average_price FLOAT NOT null,
    total_volume FLOAT NOT null,
    type varchar(50) NOT null,
    YEAR INT NOT null, 
    region varchar(40) NOT NULL
);

INSERT INTO avocado(avocado_date)
(SELECT avocado_date FROM staging_avocado);

INSERT INTO price(average_price)
(SELECT average_price FROM staging_avocado);

INSERT INTO avocado_price(avocado_id, price_id) 
(SELECT avocado_id, price_id FROM avocado 
INNER JOIN price ON avocado_id = price_id);

INSERT INTO date(year) 
(SELECT YEAR FROM staging_avocado);

INSERT INTO region(region_name) 
(SELECT region FROM staging_avocado);

INSERT INTO volume(total_volume) 
(SELECT total_volume FROM staging_avocado);

INSERT INTO type(type_name) 
(SELECT type FROM staging_avocado);

INSERT INTO avocado_volume(avocado_id, volume_id) 
(SELECT avocado_id, volume_id FROM avocado 
INNER JOIN volume ON avocado_id = volume_id);

