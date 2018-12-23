# columns and their types, including fk relationships
from sqlalchemy import Column, Integer, String, DateTime, Boolean
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.orm import backref

# declarative base 
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime
import random

# create the base class (declarative base)
# call it Base!
Base = declarative_base()

# implement the following three classes

class Scooter(Base): 
    __tablename__ = 'scooter'

    scooter_id = Column('scooter_id', Integer, primary_key = True)
    acquired_date = Column('acquired_date', DateTime(timezone=False), default=datetime.now())
    retired = Column('retired', Boolean, default = False)
    scooter_type_id = Column(Integer, ForeignKey('scooter_type.scooter_type_id'))

    scooter_type = relationship('ScooterType', uselist = False, back_populates = 'scooter' )

    def to_dict(self): 
        scooter_dict = {}
        scooter_dict['acquired_date'] = self.acquired_date.strftime('%Y-%m-%d')
        scooter_dict['retired'] = self.retired 
        scooter_dict['scooter_type'] = self.scooter_type.model
        scooter_dict['max_speed'] = self.scooter_type.max_speed 
        scooter_dict['weight'] = self.scooter_type.weight 
        scooter_dict['manufacturer'] = self.scooter_type.manufacturer.name
        scooter_dict['website'] = self.scooter_type.manufacturer.website
        return scooter_dict

    # getters and setters 
    def getAcquired_date(self): 
        return self.acquired_date

    def setAcquired_date(self, acquired_date): 
        self.acquired_date = acquired_date

    def getRetired(self): 
        return self.retired
    
    def setRetired(self, retired): 
        self.retired = retired

    def getTypeid(self): 
        return self.scooter_type_id 
    
    def setTypeid(self, scooter_type_id): 
        self.scooter_type_id = scooter_type_id

    def __repr__(self): 
        return f'{self.scooter_id}: {self.retired} - {self.acquired_date}'
    
    def __str__(self): 
        return self.__repr__()

class ScooterType(Base): 
    __tablename__ = 'scooter_type'

    scooter_type_id = Column('scooter_type_id', Integer, primary_key = True)
    model = Column('model', String)
    max_range = Column('max_range', Integer)
    weight = Column('weight', Integer)
    max_speed = Column('max_speed', Integer)

    company_id = Column(Integer, ForeignKey('company.company_id'))
    scooter = relationship('Scooter', back_populates = 'scooter_type')
    manufacturer = relationship('Company', back_populates = 'scooter_types')

    def manu(self):
        manufacturer =  self.company

    def __repr__(self): 
        return f'manufacturer: {self.manufacturer} model: {self.model} - max speed: {self.max_speed} - weight: {self.weight}'

    def __str__(self): 
        return self.__repr__()

class Company(Base): 
    __tablename__ = 'company'

    company_id = Column('company_id',  Integer, primary_key = True)
    name = Column('name', String)
    website = Column('website', String)
    founded = Column('founded', Integer)

    scooter_types = relationship('ScooterType', back_populates = 'manufacturer') 

    def __repr__(self): 
        return f'{self.name} - {self.website} - {self.founded}'

    def __str__(self): 
        return self.__repr__()




