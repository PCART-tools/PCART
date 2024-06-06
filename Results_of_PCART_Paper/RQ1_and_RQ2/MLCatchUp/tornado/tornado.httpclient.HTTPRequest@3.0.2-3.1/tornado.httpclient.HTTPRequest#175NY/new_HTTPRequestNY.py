import tornado.httpclient
request = tornado.httpclient.HTTPRequest('http://httpbin.org/get', 'GET', {'Content-Type': 'application/json'}, None, None, None, 20, 20, None, True, 5, 'MyUserAgent', True, None, streaming_callback=None, header_callback=None, prepare_curl_callback=None, proxy_host=None, auth_mode=None)
