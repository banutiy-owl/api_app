import random
from datetime import datetime
from sqlalchemy import create_engine, Column, Integer, String, Date
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class Test(Base):
    __tablename__ = 'list_books'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    description = Column(String)
    year = Column(Date)

engine = create_engine('sqlite:///books.db')
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()

random.seed(42) 
test_data = [
    {"name": "Book1", "description": "Description1", "year": datetime(2023, 1, 1)},
    {"name": "Book2", "description": "Description2", "year": datetime(2023, 1, 1)},
]

for data in test_data:
    new_book = Test(name=data['name'], description=data['description'], year=data['year'])
    session.add(new_book)

session.commit()
session.close()
