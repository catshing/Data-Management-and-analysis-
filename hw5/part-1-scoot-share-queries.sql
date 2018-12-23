part-1-scoot-share-queries.sql

1. select CustomerInfo.firstName, CustomerInfo.lastName from CustomerInfo 
   inner join ScooterReturn on CustomerInfo.customer_id = ScooterReturn.customer_id 
   where ScooterReturn.flag = ‘Yes’;

2. select * from ScooterInfo where available = ‘Yes;
      
3. select si.manufacturer, si.modelNumber, bi.timeNeedReturn, ci.firstName, ci.lastName from ScooterInfo si
   inner join BorrowInfo bi on si.scooter_id = bj.scooter_id  
   inner join CustomerInfo ci on bi.customer_id = ci.customer_id
   group by si.manufacturer, si.modelName, bi.timeNeedReturn, ci.firstName, ci.lastName;

4. select si.manufacturer, si.modelNumber, ci.firstName, ci.lastName from ScooterInfo si
   inner join BorrowInfo bi on sm.scooter_id = bi.scooter_id  
   inner join CustomerInfo ci
   inner join ScooterReturn sr on bi.scooter_id = sr.scooter_id
   where sr.isLate = ‘Yes’ 
   group by  si.manufacturer, si.modelNumber, ci.firstName, ci.lastName;


5. select firstName, lastName, count(*) from CustomerReferredBy 
   group by firstName, lastName
   order by count(*) desc 
   limit 5;

6. select customer_id, DATE(timeBorrowed) as date from BorrowInfo 
    group by customer_id, data
    order by date ASC;

7. select borrow_id, lateDamageFees from ScooterReturn 
   group by borrowid, lateDamageFees;

8. select manufacuturer from ScooterInfo;