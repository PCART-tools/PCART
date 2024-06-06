import tornado.httpclient
request = tornado.httpclient.HTTPRequest(url='http://httpbin.org/get', method='GET', headers={'Content-Type': 'application/json'}, body=None, auth_username=None, auth_password=None, connect_timeout=20, request_timeout=20, auth_mode=None)
