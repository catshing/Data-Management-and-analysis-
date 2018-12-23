-- write your queries underneath each number:
 
-- 1. the total number of rows in the database

SELECT count(*) as num_rows FROM create_table;

-- 2. show the first 15 rows, but only display 3 columns (your choice)

 SELECT year, country, region FROM create_table LIMIT 15;

-- 3. do the same as above, but chose a column to sort on, and sort in descending order

SELECT year, country, region FROM create_table ORDER BY year DESC LIMIT 15;

-- 4. add a new column without a default value

ALTER TABLE create_table ADD COLUMN new_column INTEGER;

-- 5. set the value of that new column

UPDATE create_table SET new_column = 3;

-- 6. show only the unique (non duplicates) of a column of your choice

SELECT DISTINCT(region) FROM create_table;

-- 7.group rows together by a column value (your choice) and use an aggregate function to calculate something about that group 

SELECT region, COUNT(*) FROM create_table GROUP BY region;
-- 8. now, using the same grouping query or creating another one, find a way to filter the query results based on the values for the groups 

SELECT region, COUNT(*) FROM create_table WHERE year > 2000 GROUP BY region;

-- 9. write a comment about your query 9

SELECT region, SUM(no_kills) as num_kills, SUM(multiple) as num_multipleTerrorists, SUM(suicide) as num_suicideTerrorists FROM create_table WHERE year = 2003 GROUP BY region;

-- 10. write a comment about your query 10

SELECT country, SUM(no_kills) as num_kills FROM create_table GROUP BY country ORDER BY num_kills DESC LIMIT 10;

-- 11. write a comment about your query 11

SELECT year, SUM(success) as successful_attacks FROM create_table GROUP BY year ORDER BY successful_attacks DESC LIMIT 10;
-- 12. write a comment about your query 12

SELECT city, COUNT(city) as city_counts FROM create_table WHERE country = 'UNITED STATES' GROUP BY city ORDER BY city_counts DESC LIMIT 10;

