'''
Created on Dec 2, 2012

@author: superjom
'''
#from model import Date, CalItem
from datetime import datetime
from model import *

from sqlalchemy.orm import sessionmaker
Session = sessionmaker(bind=engine)
session = Session()

t = datetime.today()
d = Date(t)

d.items = [
    CalItem('Cal1', t, t),
    CalItem('Cal1', t+1, t+1),
]
session.cr



