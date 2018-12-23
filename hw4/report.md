# Overview

I downloaded the full data from Global Terrorism Database(GTD), which is an open-source database which has records of terrorist events. It is one of the most comprehensive unclassified database of terrorist events around the world. The csv file that I downloaded has over 180,000 records of terroris incidents and attacks from all over the world internationally and domestically in the US as well. The information contained in the file is based on reports from a wide range of open media sources (over 4,000,000 news articles and 25,000 news articles were reviewed to collect the data) and the GTB team only added records only if they are credible and verified. Due to the transfer of the data in 1993, a lot of data in 1993 was missing but the GPB team decided to not include the data in 1993.

The Pinkerton Global Intelligence Services(PGIS) identified and recorded terrorism incidents from governemnt reports, wire services, and top international newspaper to determine the level of terrorism from 1970 to 1997. The Global Terrorism Database (GTD) started in 2001 when researched at University of Maryland took over the database from PGIS. The Department of Homeland Security provided additional funding to GTD from 1997.

GTD team utilises a wide range of news media sources for the identification of the incidents by using machine learning and and data mining techniques to identify types of terrorist incidents in news articles and also developed a Data Management System to compile the database.

The csv file that I used was an updated version after I dropped the columns that I did not need and the columns that were useful to what I wanted to find remained. I also cleaned up the data fields by renaming them so that it is easier to read and understand. The data fields that are contained in the updated are: 

year - year of the terrorist attack

month - month of the terrorist attack

day - day of the terrorist attack

country - country of the terrorist attack

region - region of the country of attack

city - city in country of the terrorist attack

multiple - 0 means only 1 group carried out the attack and 1 means multiple people carried out the attack

success - 0 means the attack was not successful and 1 means the attack was successful

suicide - 0 means the attack was an suicide attack and 1 means it is not

no_kills - number of people died from terrorist attacks


# Table Design

Column Name         Type           Appropriate Contraints and additional information

id                 serial          NOT NULL since there won't be any missing values and tt is a serial Primary key since                                      no fields is a good candiate for a primary key. I used a serial numeric type as an                                         artifical primary key so each row has an unique id

year               INTEGER         NOT NULL since there won't be any missing values in the column 

month              INTEGER         NOT NULL since there won't be any missing values in the column 

day                INTEGER         NOT NULL since there won't be any missing values in the column 

country            VARCHAR(50)     NOT NULL since there won't be any missing values in the column and some country names 
                                   are fairly long, so to keep it safe, I assigned the length of 50 to VARCHAR
s
region             VARCHAR(50)     NOT NULL since there won't be any missing values in the column and some region names 
                                   are fairly long, so to keep it safe, I assigned the length of 50 to VARCHAR

city               VARCHAR(50      NULL because there are missing values in the column and so to keep it safe, I                                              assignedthe length of 50 to VARCHAR

multiple           INTEGER         NULL because there are missing values in the column 

suicide            INTEGER         NULL because there are missing values in the column 

no_kills           INTEGER         NULL because there are missing values in the column

# Import

At first when I imported the cvs file, there were a lot of errors showing up such as wrong data types and there are also some errors on formatting on the csv file as well. Therefore, I looked up the mapping for the data types of the fields on the official website of Postgresql so that I could eliminate the inaccuracy of the mapping. I also converted the csv file to a txt file and I found it easier to import it with a txt file. It worked right away after I changed the data types and the txt file. 

# Database Information

```

1. Show all of databases in my postgres instance 


\l


                                   List of databases
      Name      |     Owner      | Encoding |   Collate   |    Ctype    |   Access privileges   
----------------+----------------+----------+-------------+-------------+-----------------------
 catherineshing | catherineshing | UTF8     | en_US.UTF-8 | en_US.UTF-8 | 
 homework04     | catherineshing | UTF8     | en_US.UTF-8 | en_US.UTF-8 | 
 postgres       | postgres       | UTF8     | en_US.UTF-8 | en_US.UTF-8 | 
 sample_db      | catherineshing | UTF8     | en_US.UTF-8 | en_US.UTF-8 | 
 template0      | postgres       | UTF8     | en_US.UTF-8 | en_US.UTF-8 | =c/postgres          +
                |                |          |             |             | postgres=CTc/postgres
 template1      | postgres       | UTF8     | en_US.UTF-8 | en_US.UTF-8 | =c/postgres          +
                |                |          |             |             | postgres=CTc/postgres
(6 rows)

```
```

2. Show all of the tables in my database 

\dt

               List of relations
 Schema |     Name     | Type  |     Owner      
--------+--------------+-------+----------------
 public | create_table | table | catherineshing
(1 row)
```
```

3. Show some information about the table you created and imported data into: find a way to show its columns, types and constraints 

\d create_table

                                    Table "public.create_table"
  Column  |         Type          | Collation | Nullable |                 Default                  
----------+-----------------------+-----------+----------+------------------------------------------
 id       | integer               |           | not null | nextval('create_table_id_seq'::regclass)
 year     | integer               |           | not null | 
 month    | integer               |           | not null | 
 day      | integer               |           | not null | 
 country  | character varying(50) |           | not null | 
 region   | character varying(50) |           | not null | 
 city     | character varying(50) |           |          | 
 multiple | integer               |           |          | 
 success  | integer               |           |          | 
 suicide  | integer               |           |          | 
 no_kills | integer               |           |          | 
Indexes:
    "create_table_pkey" PRIMARY KEY, btree (id)

```


# Query Results

```
### 1. The total number of rows in the table is 181691 as shown below since I count the number of rows there are in the table.

 num_rows 
----------
   181691
(1 row)

```

```
### 2. I displayed columns of year, country and region. I used LIMIT to get the first 15 rows of the table.

 year |      country       |     region     
------+--------------------+----------------
 1970 | MEXICO             | North America
 1970 | PHILIPPINES        | Southeast Asia
 1970 | GREECE             | Western Europe
 1970 | JAPAN              | East Asia
 1970 | UNITED STATES      | North America
 1970 | UNITED STATES      | North America
 1970 | URUGUAY            | South America
 1970 | UNITED STATES      | North America
 1970 | UNITED STATES      | North America
 1970 | UNITED STATES      | North America
 1970 | UNITED STATES      | North America
 1970 | ITALY              | Western Europe
 1970 | UNITED STATES      | North America
 1970 | UNITED STATES      | North America
 1970 | EAST GERMANY (GDR) | Eastern Europe
(15 rows)

```

``` 
### 3. I used the same columns as above but I did the top 15 rows in descending order. 

 year |             country              |           region           
------+----------------------------------+----------------------------
 2017 | ITALY                            | Western Europe
 2017 | BAHRAIN                          | Middle East & North Africa
 2017 | DEMOCRATIC REPUBLIC OF THE CONGO | Sub-Saharan Africa
 2017 | PAKISTAN                         | South Asia
 2017 | SOMALIA                          | Sub-Saharan Africa
 2017 | AFGHANISTAN                      | South Asia
 2017 | IRAQ                             | Middle East & North Africa
 2017 | DEMOCRATIC REPUBLIC OF THE CONGO | Sub-Saharan Africa
 2017 | TURKEY                           | Middle East & North Africa
 2017 | SYRIA                            | Middle East & North Africa
 2017 | TURKEY                           | Middle East & North Africa
 2017 | TURKEY                           | Middle East & North Africa
 2017 | PAKISTAN                         | South Asia
 2017 | YEMEN                            | Middle East & North Africa
 2017 | MYANMAR                          | Southeast Asia
(15 rows)

```

```
### 4. The results only shows ALTER TABLE since the table has been transformed because another column is added.

ALTER TABLE

```

```
### 5. After setting the value to 3 for the new column, the results show UPDATE 181691 since 181691 rows were updated after the change. 

UPDATE 181691

```

```
### 6. Below shows the distinct/unique values of the region column so all the unique regions

           region            
-----------------------------
 Middle East & North Africa
 Eastern Europe
 South America
 South Asia
 Sub-Saharan Africa
 East Asia
 North America
 Australasia & Oceania
 Central America & Caribbean
 Southeast Asia
 Central Asia
 Western Europe
(12 rows)

```

```
### 7. Below shows the number of attacks in each region by using group by region in order to group the regions together. 

           region            | count 
-----------------------------+-------
 Australasia & Oceania       |   282
 Central America & Caribbean | 10344
 Central Asia                |   563
 East Asia                   |   802
 Eastern Europe              |  5144
 Middle East & North Africa  | 50474
 North America               |  3456
 South America               | 18978
 South Asia                  | 44974
 Southeast Asia              | 12485
 Sub-Saharan Africa          | 17550
 Western Europe              | 16639
(12 rows)

```
```
### 8. Below shows the same results as above except that I have filtered the year to results that are larger than year 2000

           region            | count 
-----------------------------+-------
 Australasia & Oceania       |    69
 Central America & Caribbean |    75
 Central Asia                |   207
 East Asia                   |   179
 Eastern Europe              |  3779
 Middle East & North Africa  | 40806
 North America               |   607
 South America               |  2358
 South Asia                  | 36855
 Southeast Asia              |  9306
 Sub-Saharan Africa          | 12853
 Western Europe              |  2947
(12 rows) 

```
```
### 9. Since the Iraq War began in 2003, I want to find out the number of people died, the number of terrorists who carried out attacks with 1 or more people and the number of terrorists who were suicide bombers in the year of 2003. This 
clearly shows that the Middle East has the highest rates for all three columns and following is South Asia. I'm surprised that Africa had a lower rate than South Asia since I thought it was less stable than South Asia. (just my opinion only)

           region            | num_kills | num_multipleterrorists | num_suicideterrorists 
-----------------------------+-----------+------------------------+-----------------------
 Australasia & Oceania       |         1 |                      0 |                     0
 Central America & Caribbean |         5 |                      4 |                     0
 Central Asia                |         1 |                      0 |                     0
 East Asia                   |         1 |                      2 |                     0
 Eastern Europe              |       337 |                      8 |                    10
 Middle East & North Africa  |      1063 |                     42 |                    65
 North America               |         2 |                      9 |                     0
 South America               |       191 |                     26 |                     3
 South Asia                  |       802 |                     41 |                     8
 Southeast Asia              |       354 |                     21 |                     3
 Sub-Saharan Africa          |       555 |                     11 |                     0
 Western Europe              |         5 |                     51 |                     0

 ```
```
###10. Below shows the top 10 countries in Descending order on number of people who were killed during 1970 to 2017. (except 1993 since data was lost in the database of US government). It can be seen that the top 10 countries are mostly less developed countries in the Middle East and South Asia. I'm surprised that Syria was on the list since I thought the country was more peaceful than in recent times, but the data clearly shows that the violent upheaval started way back in 2003 already. 

   country   | num_kills 
-------------+-----------
 IRAQ        |     78589
 AFGHANISTAN |     39384
 PAKISTAN    |     23822
 NIGERIA     |     22682
 INDIA       |     19341
 SRI LANKA   |     15500
 SYRIA       |     15229
 COLOMBIA    |     14698
 PERU        |     12771
 EL SALVADOR |     12053
(10 rows)

```
```
### 11. The data below shows the top 10 most successful attacks in descending order from 1970 to 2017. The number of attacks in recent times increased dramatically. One of the dates that is shown on the list is 1992 and I wonder what happened during that time since the other top 9 years are all in the 20th century. 

 year | successful_attacks 
------+--------------------
 2014 |              15015
 2015 |              12676
 2016 |              10975
 2013 |              10484
 2017 |               8652
 2012 |               7600
 2011 |               4606
 1992 |               4560
 2009 |               4429
 2008 |               4402
(10 rows)

```
```
### 12. I wanted to find out the count of cities in the United States that the terrorist attacks took place. Therefore, I used count to find out the count of cities in United States in descending order. I'm not surprised that New York City has the highest count since it is regarded as one of the most dangerous cities in America due to the large population of people living there and it's very densely populated as well. 

     city      | city_counts 
---------------+-------------
 New York City |         460
 San Juan      |         116
 Los Angeles   |         109
 San Francisco |          98
 Washington    |          85
 Miami         |          85
 Chicago       |          57
 Seattle       |          39
 Berkeley      |          33
 Denver        |          23
(10 rows)

```

















