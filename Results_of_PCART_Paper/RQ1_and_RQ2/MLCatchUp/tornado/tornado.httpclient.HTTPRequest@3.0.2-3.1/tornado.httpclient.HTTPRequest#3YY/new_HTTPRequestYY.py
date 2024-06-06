import tornado.httpclient
request = tornado.httpclient.HTTPRequest('http://httpbin.org/get', 'GET', auth_mode=None)
