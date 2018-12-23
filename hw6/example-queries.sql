# Number 1, 2, 3, 4

-- 1.
SELECT s.scooter_id, c.founded, st.model, st.weight, st.max_speed, s.acquired_date, s.retired 
FROM scooter s INNER JOIN scooter_type st
ON s.scooter_id = st.scooter_type_id
INNER JOIN company c 
ON s.scooter_id = c.company_id 
GROUP BY s.scooter_id, c.founded, st.model, st.weight, st.max_speed, s.acquired_date, s.retired 
LIMIT 10;

-- 2.
select retired, count(retired)
from scooter 
group by retired;

-- 3.
select to_char(acquired_date, ‘YYYY-MM’) as , count(*) from scooter 
group by to_char(acquired_date ‘ YYYY-MM’);

-- 4. 
select c.company_id, count(st.scooter_type_id) 
from company c inner join scooterType st 
on c.company_id = st.company_id
group by c.company_id;




