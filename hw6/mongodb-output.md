## mongodb queries: 

1. This query is to find all the scooters that have max speed of over 600 - filter results based on exactly property (max_speed) and also show all properties

```
db.scooters.find({"max_speed": {$gte: 600}})

{ "_id" : ObjectId("5c09d2f6bc6b123ed8882bd8"), "acquired_date" : "2017-11-08", "retired" : true, "scooter_type" : "m7", "max_speed" : 750, "weight" : 500, "manufacturer" : "Tesla", "website" : "www.tesla.com" }
{ "_id" : ObjectId("5c09d2f6bc6b123ed8882bdb"), "acquired_date" : "2014-01-23", "retired" : true, "scooter_type" : "m7", "max_speed" : 750, "weight" : 500, "manufacturer" : "Tesla", "website" : "www.tesla.com" }
{ "_id" : ObjectId("5c09d2f6bc6b123ed8882be2"), "acquired_date" : "2016-11-01", "retired" : true, "scooter_type" : "m7", "max_speed" : 750, "weight" : 500, "manufacturer" : "Tesla", "website" : "www.tesla.com" }
{ "_id" : ObjectId("5c09d2f6bc6b123ed8882bf5"), "acquired_date" : "2017-03-16", "retired" : false, "scooter_type" : "m7", "max_speed" : 750, "weight" : 500, "manufacturer" : "Tesla", "website" : "www.tesla.com" }
{ "_id" : ObjectId("5c09d2f6bc6b123ed8882bfa"), "acquired_date" : "2016-11-19", "retired" : true, "scooter_type" : "m7", "max_speed" : 750, "weight" : 500, "manufacturer" : "Tesla", "website" : "www.tesla.com" }
{ "_id" : ObjectId("5c09d2f6bc6b123ed8882c03"), "acquired_date" : "2016-01-01", "retired" : true, "scooter_type" : "m7", "max_speed" : 750, "weight" : 500, "manufacturer" : "Tesla", "website" : "www.tesla.com" }

```

2. This query only shows a subset of all properties ( id, acquired_date, manufacturer) and exclude properties such as retired, scooter_type, max_speed, weight and website and then shows the first 10 documents as well 

```

db.scooters.find({}, {retired:0, scooter_type:0, max_speed:0, weight:0, website:0}).limit(10)

{ "_id" : ObjectId("5c09d2f6bc6b123ed8882bc0"), "acquired_date" : "2016-04-25", "manufacturer" : "Apple" }
{ "_id" : ObjectId("5c09d2f6bc6b123ed8882bc1"), "acquired_date" : "2016-04-22", "manufacturer" : "Apple" }
{ "_id" : ObjectId("5c09d2f6bc6b123ed8882bc2"), "acquired_date" : "2016-08-18", "manufacturer" : "Facebook" }
{ "_id" : ObjectId("5c09d2f6bc6b123ed8882bc3"), "acquired_date" : "2018-04-10", "manufacturer" : "Apple" }
{ "_id" : ObjectId("5c09d2f6bc6b123ed8882bc4"), "acquired_date" : "2018-07-19", "manufacturer" : "Tesla" }
{ "_id" : ObjectId("5c09d2f6bc6b123ed8882bc5"), "acquired_date" : "2016-02-07", "manufacturer" : "Netflix" }
{ "_id" : ObjectId("5c09d2f6bc6b123ed8882bc6"), "acquired_date" : "2018-07-03", "manufacturer" : "Apple" }
{ "_id" : ObjectId("5c09d2f6bc6b123ed8882bc7"), "acquired_date" : "2014-04-09", "manufacturer" : "Facebook" }
{ "_id" : ObjectId("5c09d2f6bc6b123ed8882bc8"), "acquired_date" : "2016-02-08", "manufacturer" : "Apple" }
{ "_id" : ObjectId("5c09d2f6bc6b123ed8882bc9"), "acquired_date" : "2015-01-09", "manufacturer" : "Facebook" }

```

3. This query matches on 2 properties (manufactuer and retired) and then exclude some properties such as _id, weight and manufacturer 

```

db.scooters.find( {"manufacturer": "Netflix", "retired": false}, {_id: 0, weight:0, manufacturer:0}) 
{ "acquired_date" : "2016-02-07", "retired" : false, "scooter_type" : "m8", "max_speed" : 450, "website" : "www.netflix.com" }
{ "acquired_date" : "2014-03-21", "retired" : false, "scooter_type" : "m4", "max_speed" : 400, "website" : "www.netflix.com" }
{ "acquired_date" : "2018-07-12", "retired" : false, "scooter_type" : "m4", "max_speed" : 400, "website" : "www.netflix.com" }
{ "acquired_date" : "2015-10-06", "retired" : false, "scooter_type" : "m4", "max_speed" : 400, "website" : "www.netflix.com" }
{ "acquired_date" : "2018-07-12", "retired" : false, "scooter_type" : "m4", "max_speed" : 400, "website" : "www.netflix.com" }
{ "acquired_date" : "2015-10-19", "retired" : false, "scooter_type" : "m4", "max_speed" : 400, "website" : "www.netflix.com" }
{ "acquired_date" : "2014-12-28", "retired" : false, "scooter_type" : "m4", "max_speed" : 400, "website" : "www.netflix.com" }

```

4. This query finds all the documents which the weight is all greater than 500 

```

db.scooters.find({"weight": {$gte: 500}})

{ "_id" : ObjectId("5c09d2f6bc6b123ed8882bc5"), "acquired_date" : "2016-02-07", "retired" : false, "scooter_type" : "m8", "max_speed" : 450, "weight" : 550, "manufacturer" : "Netflix", "website" : "www.netflix.com" }
{ "_id" : ObjectId("5c09d2f6bc6b123ed8882bcf"), "acquired_date" : "2016-06-05", "retired" : true, "scooter_type" : "m8", "max_speed" : 450, "weight" : 550, "manufacturer" : "Netflix", "website" : "www.netflix.com" }
{ "_id" : ObjectId("5c09d2f6bc6b123ed8882bd6"), "acquired_date" : "2018-05-24", "retired" : true, "scooter_type" : "m8", "max_speed" : 450, "weight" : 550, "manufacturer" : "Netflix", "website" : "www.netflix.com" }
{ "_id" : ObjectId("5c09d2f6bc6b123ed8882bd8"), "acquired_date" : "2017-11-08", "retired" : true, "scooter_type" : "m7", "max_speed" : 750, "weight" : 500, "manufacturer" : "Tesla", "website" : "www.tesla.com" }
{ "_id" : ObjectId("5c09d2f6bc6b123ed8882bdb"), "acquired_date" : "2014-01-23", "retired" : true, "scooter_type" : "m7", "max_speed" : 750, "weight" : 500, "manufacturer" : "Tesla", "website" : "www.tesla.com" }
{ "_id" : ObjectId("5c09d2f6bc6b123ed8882bdc"), "acquired_date" : "2015-11-16", "retired" : true, "scooter_type" : "m8", "max_speed" : 450, "weight" : 550, "manufacturer" : "Netflix", "website" : "www.netflix.com" }
{ "_id" : ObjectId("5c09d2f6bc6b123ed8882be2"), "acquired_date" : "2016-11-01", "retired" : true, "scooter_type" : "m7", "max_speed" : 750, "weight" : 500, "manufacturer" : "Tesla", "website" : "www.tesla.com" }
{ "_id" : ObjectId("5c09d2f6bc6b123ed8882be6"), "acquired_date" : "2016-09-16", "retired" : true, "scooter_type" : "m8", "max_speed" : 450, "weight" : 550, "manufacturer" : "Netflix", "website" : "www.netflix.com" }
{ "_id" : ObjectId("5c09d2f6bc6b123ed8882bf5"), "acquired_date" : "2017-03-16", "retired" : false, "scooter_type" : "m7", "max_speed" : 750, "weight" : 500, "manufacturer" : "Tesla", "website" : "www.tesla.com" }
{ "_id" : ObjectId("5c09d2f6bc6b123ed8882bfa"), "acquired_date" : "2016-11-19", "retired" : true, "scooter_type" : "m7", "max_speed" : 750, "weight" : 500, "manufacturer" : "Tesla", "website" : "www.tesla.com" }
{ "_id" : ObjectId("5c09d2f6bc6b123ed8882c02"), "acquired_date" : "2016-03-17", "retired" : true, "scooter_type" : "m8", "max_speed" : 450, "weight" : 550, "manufacturer" : "Netflix", "website" : "www.netflix.com" }
{ "_id" : ObjectId("5c09d2f6bc6b123ed8882c03"), "acquired_date" : "2016-01-01", "retired" : true, "scooter_type" : "m7", "max_speed" : 750, "weight" : 500, "manufacturer" : "Tesla", "website" : "www.tesla.com" }

```


5.  This query shows all the docuemnts that have the manufacturer equals Apple or website equals www.tesla.com 

```

db.scooters.find( {"$or" : [{"manufacturer" : "Apple"}, {"website": "www.tesla.com"}]})

{ "_id" : ObjectId("5c09d2f6bc6b123ed8882bc0"), "acquired_date" : "2016-04-25", "retired" : true, "scooter_type" : "m2", "max_speed" : 300, "weight" : 250, "manufacturer" : "Apple", "website" : "wwww.apple.com" }
{ "_id" : ObjectId("5c09d2f6bc6b123ed8882bc1"), "acquired_date" : "2016-04-22", "retired" : false, "scooter_type" : "m2", "max_speed" : 300, "weight" : 250, "manufacturer" : "Apple", "website" : "wwww.apple.com" }
{ "_id" : ObjectId("5c09d2f6bc6b123ed8882bc3"), "acquired_date" : "2018-04-10", "retired" : false, "scooter_type" : "m6", "max_speed" : 250, "weight" : 450, "manufacturer" : "Apple", "website" : "wwww.apple.com" }
{ "_id" : ObjectId("5c09d2f6bc6b123ed8882bc4"), "acquired_date" : "2018-07-19", "retired" : true, "scooter_type" : "m3", "max_speed" : 250, "weight" : 300, "manufacturer" : "Tesla", "website" : "www.tesla.com" }
{ "_id" : ObjectId("5c09d2f6bc6b123ed8882bc6"), "acquired_date" : "2018-07-03", "retired" : true, "scooter_type" : "m6", "max_speed" : 250, "weight" : 450, "manufacturer" : "Apple", "website" : "wwww.apple.com" }
{ "_id" : ObjectId("5c09d2f6bc6b123ed8882bc8"), "acquired_date" : "2016-02-08", "retired" : false, "scooter_type" : "m5", "max_speed" : 450, "weight" : 400, "manufacturer" : "Apple", "website" : "wwww.apple.com" }
{ "_id" : ObjectId("5c09d2f6bc6b123ed8882bca"), "acquired_date" : "2015-01-06", "retired" : true, "scooter_type" : "m6", "max_speed" : 250, "weight" : 450, "manufacturer" : "Apple", "website" : "wwww.apple.com" }
{ "_id" : ObjectId("5c09d2f6bc6b123ed8882bd1"), "acquired_date" : "2018-08-09", "retired" : false, "scooter_type" : "m6", "max_speed" : 250, "weight" : 450, "manufacturer" : "Apple", "website" : "wwww.apple.com" }
{ "_id" : ObjectId("5c09d2f6bc6b123ed8882bd3"), "acquired_date" : "2017-03-19", "retired" : true, "scooter_type" : "m2", "max_speed" : 300, "weight" : 250, "manufacturer" : "Apple", "website" : "wwww.apple.com" }
{ "_id" : ObjectId("5c09d2f6bc6b123ed8882bd5"), "acquired_date" : "2015-06-19", "retired" : false, "scooter_type" : "m3", "max_speed" : 250, "weight" : 300, "manufacturer" : "Tesla", "website" : "www.tesla.com" }
{ "_id" : ObjectId("5c09d2f6bc6b123ed8882bd8"), "acquired_date" : "2017-11-08", "retired" : true, "scooter_type" : "m7", "max_speed" : 750, "weight" : 500, "manufacturer" : "Tesla", "website" : "www.tesla.com" }
{ "_id" : ObjectId("5c09d2f6bc6b123ed8882bd9"), "acquired_date" : "2018-12-01", "retired" : true, "scooter_type" : "m3", "max_speed" : 250, "weight" : 300, "manufacturer" : "Tesla", "website" : "www.tesla.com" }
{ "_id" : ObjectId("5c09d2f6bc6b123ed8882bda"), "acquired_date" : "2016-04-11", "retired" : true, "scooter_type" : "m2", "max_speed" : 300, "weight" : 250, "manufacturer" : "Apple", "website" : "wwww.apple.com" }
{ "_id" : ObjectId("5c09d2f6bc6b123ed8882bdb"), "acquired_date" : "2014-01-23", "retired" : true, "scooter_type" : "m7", "max_speed" : 750, "weight" : 500, "manufacturer" : "Tesla", "website" : "www.tesla.com" }
{ "_id" : ObjectId("5c09d2f6bc6b123ed8882bdf"), "acquired_date" : "2015-07-19", "retired" : true, "scooter_type" : "m3", "max_speed" : 250, "weight" : 300, "manufacturer" : "Tesla", "website" : "www.tesla.com" }
{ "_id" : ObjectId("5c09d2f6bc6b123ed8882be0"), "acquired_date" : "2014-09-02", "retired" : false, "scooter_type" : "m6", "max_speed" : 250, "weight" : 450, "manufacturer" : "Apple", "website" : "wwww.apple.com" }
{ "_id" : ObjectId("5c09d2f6bc6b123ed8882be1"), "acquired_date" : "2014-08-23", "retired" : true, "scooter_type" : "m2", "max_speed" : 300, "weight" : 250, "manufacturer" : "Apple", "website" : "wwww.apple.com" }
{ "_id" : ObjectId("5c09d2f6bc6b123ed8882be2"), "acquired_date" : "2016-11-01", "retired" : true, "scooter_type" : "m7", "max_speed" : 750, "weight" : 500, "manufacturer" : "Tesla", "website" : "www.tesla.com" }
{ "_id" : ObjectId("5c09d2f6bc6b123ed8882be4"), "acquired_date" : "2017-12-06", "retired" : true, "scooter_type" : "m6", "max_speed" : 250, "weight" : 450, "manufacturer" : "Apple", "website" : "wwww.apple.com" }
{ "_id" : ObjectId("5c09d2f6bc6b123ed8882be7"), "acquired_date" : "2014-04-25", "retired" : false, "scooter_type" : "m2", "max_speed" : 300, "weight" : 250, "manufacturer" : "Apple", "website" : "wwww.apple.com" }

```



