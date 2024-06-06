import aiohttp
session = aiohttp.ClientSession()
url = 'ws://example.com/socket'
protocols = ('chat',)
timeout = 10.0
autoclose = False
autoping = True
auth = aiohttp.BasicAuth('username', 'password')
origin = 'http://example.com'
websocket = session.ws_connect(url, timeout=timeout, auth=auth, protocols=protocols, autoping=autoping, autoclose=autoclose, headers=None)
