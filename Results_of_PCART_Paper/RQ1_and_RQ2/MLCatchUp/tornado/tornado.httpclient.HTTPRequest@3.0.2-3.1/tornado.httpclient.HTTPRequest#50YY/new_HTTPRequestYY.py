import tornado.httpclient
request = tornado.httpclient.HTTPRequest('http://httpbin.org/get', 'GET', {'Content-Type': 'application/json'}, None, auth_username=None, auth_password=None, connect_timeout=20, request_timeout=20, if_modified_since=None, auth_mode=None)
