import tornado.httpclient
request = tornado.httpclient.HTTPRequest('http://httpbin.org/get', 'GET', {'Content-Type': 'application/json'}, None, None, auth_password=None, connect_timeout=20, request_timeout=20, auth_mode=None)
