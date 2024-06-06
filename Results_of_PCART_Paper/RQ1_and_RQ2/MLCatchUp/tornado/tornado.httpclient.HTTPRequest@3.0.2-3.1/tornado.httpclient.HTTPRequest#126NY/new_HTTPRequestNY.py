import tornado.httpclient
request = tornado.httpclient.HTTPRequest('http://httpbin.org/get', 'GET', {'Content-Type': 'application/json'}, None, None, None, 20, 20, None, follow_redirects=True, max_redirects=5, user_agent='MyUserAgent', use_gzip=True, network_interface=None, streaming_callback=None, auth_mode=None)
