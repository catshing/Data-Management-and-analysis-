from sqlalchemy.orm import sessionmaker
import db
from model import Company, ScooterType, Scooter, Base
import json

Session = sessionmaker(db.engine)
session = Session()

scooters = session.query(Scooter)
scooters_as_dicts = [s.to_dict() for s in scooters]

session.close()

with open('scooters.json', 'w') as f:
    # TO DEBUG: uncomment this line...
    # print(json.dumps(scooters_as_dicts))
    s = json.dump(scooters_as_dicts, f)
