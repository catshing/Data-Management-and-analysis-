from sqlalchemy.orm import sessionmaker
import db
from model import Company, ScooterType, Scooter, Base
from datetime import datetime
import random

Session = sessionmaker(db.engine)
session = Session()

# use the session object and imported classes (Company, Scooter, etc.)
# ... to create companies, types and scooters in the database

c1 = Company()
c1.name = 'Facebook'
c1.website = 'www.facebook.com'
c1.founded = 2001

c2 = Company() 
c2.name = 'Apple'
c2.website = 'wwww.apple.com'
c2.founded = 1995

c3 = Company()
c3.name = 'Tesla'
c3.website = 'www.tesla.com'
c3.founded = 2007

c4 = Company()
c4.name = 'Netflix'
c4.website = 'www.netflix.com'
c4.founded = 2014

st1 = ScooterType()
st1.model = 'm1'
st1.max_range = 150
st1.weight = 200
st1.max_speed = 300
st1.manufacturer = c1
st1.company_id = random.choice([1,2,3,4])

st2 = ScooterType()
st2.model = 'm2'
st2.max_range = 200
st2.weight = 250
st2.max_speed = 300 
st2.manufacturer = c2
st2.company_id = random.choice([1,2,3,4])

st3 = ScooterType()
st3.model = 'm3'
st3.max_range = 250
st3.weight = 300
st3.max_speed = 250
st3.manufacturer = c3
st3.company_id = random.choice([1,2,3,4])

st4 = ScooterType()
st4.model = 'm4'
st4.max_range = 300 
st4.weight = 350
st4.max_speed = 400
st4.manufacturer = c4
st4.company_id = random.choice([1,2,3,4])

st5 = ScooterType()
st5.model = 'm5'
st5.max_range = 350
st5.weight = 400
st5.max_speed = 450
st5.manufacturer = c1
st5.company_id = random.choice([1,2,3,4])

st6 = ScooterType()
st6.model = 'm6'
st6.max_range = 400
st6.weight = 450 
st5.manufacturer = c2
st6.max_speed = 250
st6.company_id = random.choice([1,2,3,4])

st7 = ScooterType()
st7.model = 'm7'
st7.max_range = 450
st7.weight = 500 
st7.max_speed = 750
st7.manufacturer = c3
st7.company_id = random.choice([1,2,3,4])

st8 = ScooterType()
st8.model = 'm8'
st8.max_range = 500 
st8.weight = 550 
st8.max_speed = 450
st8.manufacturer = c4
st8.company_id = random.choice([1,2,3,4])

session.add(c1)
session.add(c2)
session.add(c3)
session.add(c4)
session.add(st1)
session.add(st2)
session.add(st3)
session.add(st4)
session.add(st5)
session.add(st6)
session.add(st7)
session.add(st8)

#create 70 objects from Scooter class
scooters = [Scooter() for i in range(70)]

#each Scooter object will be assigned to randomly generated data
for scooter in scooters: 
    date = f'{random.randint(2014,2018)}-{random.randint(1, 12):02}-{random.randint(1,28):02}'
    scooter.setAcquired_date(date)
    choice = random.choice([True, False])
    scooter.setRetired(choice)
    type_id = random.choice([1,2,3,4,5,6,7,8])
    scooter.setTypeid(type_id)
    session.add(scooter)

session.commit()

for c in session.query(Company):
    print(f'The company, {c}, has the following scooter models:')
    for i, scooter_type in enumerate(c.scooter_types):
        print(i, scooter_type)

for s in session.query(ScooterType):
    print(f'{s.manufacturer.name} ==> {s.model}')




