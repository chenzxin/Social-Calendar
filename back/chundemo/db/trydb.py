'''
Created on Dec 2, 2012

@author: superjom
'''
from datetime import date
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from table_def import Date, Item
 
engine = create_engine('sqlite:///data.db', echo=True)
 
# create a Session
Session = sessionmaker(bind=engine)
session = Session()

t = date.today()
# Create an artist
new_date = Date(t)
new_date.items = [Item("Read All About It", 
                    1,3)]
 
# add more albums
more_items = [Item("Hell Is for Wimps",
                     1,2),
               Item("Love Liberty Disco", 
                     3,4),
               Item("Thrive",
                     13,14)]
new_date.items.extend(more_items)
 
# Add the record to the session object
session.add(new_date)
# commit the record the database
session.commit()
 
# Add several artists
session.add_all([
    Date(t),
    Date(t),
    Date(t),
    ])
session.commit()
