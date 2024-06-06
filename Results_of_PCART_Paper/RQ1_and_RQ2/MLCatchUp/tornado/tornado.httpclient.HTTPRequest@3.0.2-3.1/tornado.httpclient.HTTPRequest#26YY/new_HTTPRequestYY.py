import tornado.httpclient
request = tornado.httpclient.HTTPRequest('http://httpbin.org/get', method='GET', headers={'Content-Type': 'application/json'}, body=None, auth_username=None, auth_password=None, auth_mode=None)
