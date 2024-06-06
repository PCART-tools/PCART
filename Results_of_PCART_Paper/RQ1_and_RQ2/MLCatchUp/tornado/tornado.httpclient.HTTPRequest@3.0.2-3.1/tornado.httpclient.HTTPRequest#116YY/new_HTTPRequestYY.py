import tornado.httpclient
request = tornado.httpclient.HTTPRequest('http://httpbin.org/get', 'GET', {'Content-Type': 'application/json'}, body=None, auth_username=None, auth_password=None, connect_timeout=20, request_timeout=20, if_modified_since=None, follow_redirects=True, max_redirects=5, user_agent='MyUserAgent', use_gzip=True, network_interface=None, auth_mode=None)
