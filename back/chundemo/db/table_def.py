# table_def.py
from sqlalchemy import create_engine, ForeignKey
from sqlalchemy import Column, Date, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, backref
 
engine = create_engine('sqlite:///db/data.db', echo=True)
Base = declarative_base()
 
########################################################################
class Date(Base):
    """"""
    __tablename__ = "date"
 
    id = Column(Integer, primary_key=True)
    date = Column(Date)

    def __init__(self, date):
        self.date = date
    #----------------------------------------------------------------------
 
########################################################################
class Item(Base):
    """"""
    __tablename__ = "item"
 
    id = Column(Integer, primary_key=True)
    title = Column(String)
    # start, end o'clock
    start = Column(Integer)
    end  = Column(Integer)
    # relationship
    #artist_id = Column(Integer, ForeignKey("artists.id"))
    date_id = Column(Integer, ForeignKey("date.id"))
    date = relationship("Date", backref=backref("items", order_by=id))
 
    #----------------------------------------------------------------------
    def __init__(self, title, start, end):
        self.title = title
        self.start = start
        self.end = end
 
# create tables
Base.metadata.create_all(engine)
