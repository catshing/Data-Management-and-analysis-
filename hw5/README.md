# Homework 05

## Scoot-Share

[er_diagram.png](er_diagram.png)

* TODO: a list of design decisions


In order to make sure the data model is minimally in second normal form: 

Tables in 1st normal form must follow: 
There are no repeating groups 
All the keys attributes are defined 
All attributes are dependent on the primary key

Tables in 2nd normal form must follow: 
They are in 1st normal form 
They include no partial dependencies (when an attribute is only dependent on part of a primary key)

** For an attribute to be only dependent on part of the primary key, the primary key must consist of more than 1 field. If the primary key contains only one field, the table is automatically in 2nd normal form it is in 1st normal form


References: 
https://mariadb.com/kb/en/library/database-normalization-1st-normal-form/

https://mariadb.com/kb/en/library/database-normalization-2nd-normal-form/

Firstly, in order to take down the name of the customer, contact information I first created a CustomerInfo table to store the first name, last name, time entered the store, contact details(email, address, timeEntered). Since name will have 2 values and according to the first normalization form, each column should contain atomic values so entries like first name and last name in one entry will violate the rule. Also, address can have multiple values in one entry since it will have zipcode, city, street, street name in one entry. I will create separate columns for those values in order to ensure there are atomic values for the first form normalization.
The composite keys for this table customer_id, firstName, lastName, timeEntered in order to uniquely identity each row since customer_id is not enough because there could be multiple first names and last names. Therefore, for better identification, time entered column should be included in one of the keys to ensure uniqueness. For the contact information like email, cell phone, address, street name, zip code, since they do not have to depend on the last name or time entered, I created another table called customer contact information to store the contact columns in order to remove partial dependencies. The composite keys for this column is address_id and customer_id but the email column does not depend on the address id so in order to satisfy the 2nd normalization form since it should have no partial dependencies, I created the CustomerEmail table to store the email information. Also, since the cell phone of the customer does not need to depend on the last name, I broke down the composite of the keys and created a table to store the cell phone information in order to remove partial dependencies. Also, I created one table to store customer address information and another table to store the customer email information in order to get rid of all partial dependencies so all columns will only depend on the primary key. 

I created a table for information of the scooter (ScooterInfo) which contains the range, weight, top speed, condition, country of the manufacturer of the scooter and whether the scooter is available. Since multiple scooters could have the same manufacturer and model number, I created another table for the manufacturer and model number in order to avoid redundancy of the same columns due to repeating scooters that have the same manufacturer and model number.Also to satisfy the second normalization form, all columns now in ScooterInfo and ScooterManufactured will depend on the primary keys in their tables. 

For the borrow information of the customer, I created a table to store the information of the time that the customer borrowed the scooter, time needed to return the scooter, number of hours that customers have to borrow the scooter for, and how much the service is. The primary key is borrow_id but scooter_id and scooter_id would make a more meaningful primary key because if i want to get the customer id then I can correlate to the scooter id so it is best to include both. In order to follow the rules of the forms, the columns in the BorrowInfo do not have any partial dependencies so they all depend on the primary key. It can be argued that time borrowed, time need return, number hours do no need to depend on the scooter but if one customer reserves a scooter in advance, then the time return and number of hours that the customer will need to depend on the scooter. Also, time borrowed will also need to depend on the scooter since the scooter will not be available if it wasn’t returned back previously from the previous customer. Therefore, the table is in second normalization form since there are no partial dependencies and also it is already in the first normalization form. 

When the customer returns his/her scooter, I should note down the time he returns it, whether it has any damages, whether is it a late return, and also note down any late or damage fees. Also, if the customer returns the scooter late or has any damages, then i can flag the customer so the next time he wants to borrow it, the store won’t let me. The candidate keys would be customer_id and scooter_id since they both can identify the customer’s return scooter together. The rest of the columns in the table all depend on the primary keys and there are no partial dependencies so it is already in second normalization form.

Since an arbitrary number of freeform text notes can be added to when a customer borrows a scooter, this can be 0 to many relationship. The table will store issues of the scooter while using it or issues when it’s returned (issues column) and the category of the issues.  Candidate keys could be scooter_id and customer_Id and the added columns depend on the primary keys so there are no partial dependencies since the issues and category columns will have to depend on the state of the scooter and also depend on how the customers view the scooter and its state. 

* TODO: a list of assumptions

Some of the difficulties that I came across in this assignment was to identify primary, candidate and composite keys because it can be very subjective. In the BorrowInfo table, since the composite keys are customer_id and scooter_id, others might suggest that the number of hours column might not need to depend on the scooter. However, I think that it can also depend on the scooter itself because if the scooter is not available in the store, then customers will not be able to borrow the scooter for a set number of hours. Also, if a customer reserves a scooter in advance, then the customer might have to adjust the number of hours that he/she can choose. However, others might think that customers is the sole decision maker to choose the number of hours that he/she wants to borrow the scooter for and it does not need to depend on the scooter. Also, I assume the amount paid from the same table also needs to depend on the scooter itself because I think if the scooter is of more high end collection or brand, or perhaps is newer than others, then customers will have to pay more for the particular scooter. However, others might argue that the amount paid does not need to depend on the scooter itself but by how much the customer wants to pay. Therefore, I had to use my own intuition to think it though for the partial dependencies part. Also, I broke down the composition of the keys for storing customer information into several tables (Customer Address, Customer Email, Customer Cell Phone, Customer Referred by) in order to remove partial dependencies. For the customer address table, I assumed that the addresses would be broken down into street name, city, state, zip code in order to get rid of multiple values in one entry. However, I wasn’t sure if the address should only include the zipCode or city or country. Therefore, I think identifying the keys are the most ambiguous part so by breaking down the different scenarios, it is easier to solve. 

Scripts

* [part-1-scoot-share-create.sql](part-1-scoot-share-create.sql)
* [part-1-scoot-share-queries.sql](part-1-scoot-share-queries.sql)

## Normalization

* [part-2-normalization-create.sql](part-2-normalization-create.sql)
* [part-2-normalization-import.sql](part-2-normalization-import.sql)
* [part-2-normalization-queries.sql](part-2-normalization-queries.sql)
