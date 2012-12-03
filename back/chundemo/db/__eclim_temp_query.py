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
        res = session.query(Date)[-30:]
        return res

    def getRange(self, start, end):
        '''
        @start :    datetime.date
        @end :      datetime.date
        '''
        print 'date range'
        res = session.query(Date).filter(Date.date >= start and Date.date <= end).all()
        return res

    def jsonMaper(self, datelist):
        def transTime(date, e):
            h = ''
            hour = int(e/2)
            half = e%2
            if half:
                return '%s %d:%s' % (str(date), hour, '30:00')
            else:
                return '%s %d:%s' % (str(date), hour, '00:00')

        res = []
        for d in datelist:
            date = d.date
            items = d.items
            for i in items:
                res .a
                 {
                        'id':i.id,
                        'title': i.title,
                        'start': transTime(date, i.start),
                        'end': transTime(date, i.end),
                }
        
        

if __name__ == '__main__':
    q = Query()
    #res = q.getInit()
    res = q.getRange(1,2)
    print 'dates:'
    for i in res:
        print i.date

        
        
