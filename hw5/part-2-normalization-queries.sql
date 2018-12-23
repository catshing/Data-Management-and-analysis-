//I want to find out the the correspondance between organic type avocados and region name that starts with New e.g. (New York, New Jersey)
1. SELECT t.type_name, r.region_name FROM type t
INNER JOIN region r ON t.type_id = r.region_id
WHERE r.region_name LIKE 'New%' AND t.type_name = 'organic';


//I want to know if the total volume of avocados sold each day is correlated to the average price of avocados
// so this query is to output the average price of avocados and total volume of avocados 
2. SELECT p.average_price, v.total_volume 
   FROM price p FULL JOIN volume v 
   ON p.price_id = v.volume_id;

//I want to find out the total sum of average price for each region in the States
SELECT r.region_name, SUM(p.average_price)
FROM region r INNER JOIN price p
ON r.region_id = p.price_id 
GROUP BY region_name;
   