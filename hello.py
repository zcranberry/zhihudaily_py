#encoding:UTF-8
import urllib2
import json
import tornado.ioloop
import tornado.web


headers = {'User-Agent':'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6'}
url = 'http://news.at.zhihu.com/api/1.2/news/latest'
req = urllib2.Request(url,headers = headers)
content = urllib2.urlopen(req).read()
json_cont = content.decode('u8')
loaded = json.loads(json_cont)
print loaded['date']
#for each in loaded['news']:
#    print 'title:', each['title']
#    print 'url:', each['url']

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        for each in loaded['news']:
        	self.write('<p> <a href = {0} >{1}</a></p>\n'.format(each['share_url'], each['title'].encode('utf-8')))


application = tornado.web.Application([
    (r"/", MainHandler),
])


if __name__ == "__main__":
    application.listen(8888)
    tornado.ioloop.IOLoop.instance().start()
