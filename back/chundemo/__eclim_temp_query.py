from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from table_def import Date, Item
from datetime import datetime
 
engine = create_engine('sqlite:///data.db', echo=True)

# create a Session
Session = sessionmaker(bind=engine)
session = Session()

class Query:
    def getInit(self):
        '''
        return latest calendar
        '''
        res = session.query(Date).
        
        
