import tornado.httpclient
request = tornado.httpclient.HTTPRequest(url='http://httpbin.org/get', method='GET', auth_mode=None)
