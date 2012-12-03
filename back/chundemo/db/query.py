from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from table_def import Date, Item
from datetime import datetime
from datetime import date
 

class Query:
    def __init__(self):
        engine = create_engine('sqlite:///db/data.db', echo=False)

        # create a Session
        Session = sessionmaker(bind=engine)
        self.session = Session()

    def get(self, date):
        res = self.session.query(Date).filter(Date.date == date).first()
        return res
        
    def getInit(self):
        '''
        return latest calendar
        '''
        res = self.session.query(Date)[-30:]
        return self.jsonMaper(res)

    def getRange(self, start, end):
        '''
        @start :    datetime.date
        @end :      datetime.date
        '''
        print 'date range'
        res = self.session.query(Date).filter(Date.date >= start and Date.date <= end).all()
        return self.jsonMaper(res)

    def add(self, data):
        print '-'*50
        print 'saving !!!!', data
        _datas = data['date'].split('-')
        _date = date(
            int(_datas[0]),
            int(_datas[1]),
            int(_datas[2])
        )
        da = self.get(_date)
        if not da:
            '''
            add a date
            '''
            da = Date(_date)
            #self.session.commit()
        print 'table:',da
        item = Item(data['title'], int(data['start']), int(data['end'])) 
        da.items.extend([item])
        self.session.add(da)
        self.session.add(item)
        print 'commit'
        self.session.commit()

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
                res.append({
                    'id':i.id,
                    'title': i.title,
                    'allDay':False,
                    'start': transTime(date, i.start),
                    'end': transTime(date, i.end),
                })
        return res
        

if __name__ == '__main__':
    q = Query()
    from datetime import date
    res = q.get(date(2012, 12, 3))
    #res = q.getRange(1,2)
    print 'res;'
    print res

        
        
