import tornado.httpclient
request = tornado.httpclient.HTTPRequest(url='http://httpbin.org/get', auth_mode=None)
