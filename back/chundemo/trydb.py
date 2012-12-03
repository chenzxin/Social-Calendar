'''
Created on Dec 2, 2012

@author: superjom
'''
#from model import Date, Item
from datetime import datetime
from model import *

from sqlalchemy.orm import sessionmaker
Session = sessionmaker()
Session.configure(bind=engine)
session = Session()

t = datetime.today()

d = Date(t)
print d

t1 = Item('Cal1', 3, 4)
print t1
t2 = Item('Cal2', 6, 9)

session.add(d)
session.add(t1)
session.add(t2)

#session.commit()



