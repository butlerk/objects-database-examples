# Import and call sqlalchemy functions required to write to a database file
from sqlalchemy import create_engine
engine = create_engine('sqlite:///store.db', echo=True)
from sqlalchemy.orm import declarative_base
Base = declarative_base()

# Define a class for the Fruit table, importing needed classes from SQLAlchemy
from sqlalchemy import Column, Integer, Text
class Fruit(Base):
    __tablename__ = 'fruit'
    id = Column(Integer, primary_key=True)
    name = Column(Text)
    price_cents = Column(Integer)

class Vegetable(Base):
    __tablename__ = 'vegetables'
    id = Column(Integer, primary_key=True)
    name = Column(Text)
    colour = Column(Text)
    price_cents = Column(Integer)

# Create the defined class (Fruit) as a table in the SQLite database file
Base.metadata.create_all(engine)

# Imports sqlalchemy class for creating session that connects to SQLite database
from sqlalchemy.orm import sessionmaker
# Creates a connection session with the SQLite database, so we can read and write to it
Session = sessionmaker(bind=engine)
session = Session()

# Create an apple Fruit database object and add them to the session
apple = Fruit(name='apple', price_cents=100)
session.add(apple)

# Create a pear Fruit database object and add them to the session
pear = Fruit(name='pear', price_cents=90)
session.add(pear)

# Create a banana Fruit database object and add them to the session
banana = Fruit(name='banana', price_cents=120)
session.add(banana)

# Create a carrot Vegetable database object and add them to the session
carrot = Vegetable(name='carrot', price_cents=20, colour='orange')
session.add(carrot)

potato = Vegetable(name='potato', price_cents=10, colour='brown')
session.add(potato)

broccoli = Vegetable(name='broccoli', price_cents=50, colour='green')
session.add(broccoli)


# Commit the changes made in the session (this writes the new objects to the database file)
session.commit()


# Imports sqlalchemy class for creating session that connects to SQLite database
from sqlalchemy.orm import sessionmaker
# Creates a connection session with the SQLite database, so we can read and write to it
Session = sessionmaker(bind=engine)
session = Session()

fruits = session.query(Fruit).all()

deletequsn = input('Do you wish to delete a fruit?')
if deletequsn == "Y":
    print("I am going to delete")
    choice = input("Type in a fruit to delete")
    for fruit in fruits:
        print(f"Fruit: {fruit.name}")
        if fruit.name == choice:
            print(f"Fruit name: {fruit.name}")
            print(f"Price: {fruit.price_cents}")
            
            
else:
    print("Ok, no delete")

session.commit()