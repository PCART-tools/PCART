import tornado.httpclient
request = tornado.httpclient.HTTPRequest('http://httpbin.org/get', 'GET', headers={'Content-Type': 'application/json'}, auth_mode=None)
