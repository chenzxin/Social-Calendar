'''
Created on Dec 2, 2012

@author: superjom
'''
from sqlalchemy import ForeignKey
from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()
from sqlalchemy import Column, Integer, String, DateTime, LargeBinary
from sqlalchemy import create_engine
from sqlalchemy.orm import relationship, backref

engine = create_engine('sqlite:///data.db')

class Date(Base):
    '''
    data
    flags for each day
    '''
    __tablename__ = 'date'
    id = Column(Integer, primary_key=True)
    # relation
    items = relationship("Item")
    #bdata = Column(LargeBinary(48))

    def __init__(self, date, bdata=None):
        self.date = date
        #self.bdata = bdata

class Item(Base):
    __tablename__ = 'item'
    id = Column(Integer, primary_key=True)
    title = Column(String)
    # start, end o'clock
    start = Column(Integer)
    end  = Column(Integer)
    # date.items
    #date_id = Column(Integer, ForeignKey('dates.id'))
    #date = relationship("Date", backref=backref('dates', order_by=id))

    def __init__(self, title, start, end):
        self.title = title
        self.start = start
        self.end = end


class Parent(Base):
    __tablename__ = 'parent'
    id = Column(Integer, primary_key=True)
    children = relationship("Child", backref='parent')

    def __init__(self):
        pass

class Child(Base):
    __tablename__ = 'child'
    id = Column(Integer, primary_key=True)
    parent_id = Column(Integer, ForeignKey('parent.id'))

    def __init__(self):
        

if __name__=='__main__':
    Base.metadata.create_all(engine)
