from datetime import date
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from table_def import Date, Item
from query import Query
from datetime import date
 
class CalAdd:
    def __init__(self):
        engine = create_engine('sqlite:///db/data.db', echo=True)
        # create a Session
        Session = sessionmaker(bind=engine)
        self.session = Session()
        self.q = Query()

    def add(self, data):
        print '-'*50
        print 'saving !!!!', data
        _datas = data['date'].split('-')
        _date = date(
            int(_datas[0]),
            int(_datas[1]),
            int(_datas[2])
        )
        da = self.q.get(_date)
        if not da:
            '''
            add a date
            '''
            da = Date(_date)
            #self.session.commit()
        print da
        item = Item(data['title'], int(data['start']), int(data['end'])) 
        da.items.extend([item])
        self.session.add(da)
        self.session.commit()
        

if __name__ == '__main__':
    cd = CalAdd()   
    data = {
        'title': 'hello world',
        'date': '2012-12-1',
        'start': 4,
        'end': 6
    }
    cd.add(data)

