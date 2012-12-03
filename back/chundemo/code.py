'''
Created on Dec 2, 2012

@author: superjom
'''
import web
import json
from db.query import Query
from datetime import date

render = web.template.render('templates/')
urls = [
    '/',                    'index',
    '/back/init/(.*)',  'calender',
    '/back/add/(.*)', 'caladd',
]


class index:
    def GET(self):
        hello = web.template.frender('templates/calender.html')
        return hello()

class calender:
    def __init__(self):
        pass

    def GET(self, data):
        web.header('Content-Type', 'application/json')
        data = web.input()
        query = Query()
        if data:
            _start = int(data['start'])
            _end = int(data['end'])
            res = query.getRange(date.fromtimestamp(_start), date.fromtimestamp(_end))
            return json.dumps(res)
        #print 'data' + '*'*50
        #print data
        init_res = query.getInit()
        #print json.dumps(init_res)
        return json.dumps(init_res)

from db.add import CalAdd
from datetime import date
class caladd:
    def __init__(self):
        pass
        
    def GET(self, data):
        q = Query()
        data = web.input()
        print '.. data', data
        if data:
            print '.. database: add date'
            print '.. data', data
            q.add(data)


if __name__ == '__main__':
    app = web.application(urls, globals())
    app.run()
