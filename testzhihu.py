#encoding:UTF-8
import urllib2

headers = {'User-Agent':'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6'}
#出现urllib2.HTTPError: HTTP Error 403: Forbidden错误是由于网站禁止爬虫,在请求加上头信息，伪装成浏览器访问解决
url = 'http://news.at.zhihu.com/api/1.2/news/latest'
req = urllib2.Request(url,headers = headers)
content = urllib2.urlopen(req).read()
print content.decode('u8')

