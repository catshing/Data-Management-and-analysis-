from sqlalchemy.orm import sessionmaker
import db
import model

Session = sessionmaker(db.engine)
session = Session()

model.Base.metadata.create_all(db.engine)
