import tornado.httpclient
request = tornado.httpclient.HTTPRequest('http://httpbin.org/get', 'GET', {'Content-Type': 'application/json'}, None, None, None, connect_timeout=20, request_timeout=20, if_modified_since=None, follow_redirects=True, max_redirects=5, auth_mode=None)
