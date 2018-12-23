-- write your COPY statement to import a csv here

COPY create_table (year, month, day, country, region, city, multiple, success, suicide, no_kills) FROM '/Users/catherineshing/Desktop/Data_management/catgraphics-homework03/new.txt' WITH DELIMITER ',' CSV HEADER;

