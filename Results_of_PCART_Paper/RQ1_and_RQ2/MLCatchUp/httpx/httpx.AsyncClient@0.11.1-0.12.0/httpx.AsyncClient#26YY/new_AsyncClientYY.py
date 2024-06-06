import httpx
from httpx import Auth, Timeout, PoolLimits, URL
client = httpx.AsyncClient(auth=httpx.BasicAuth('username', 'password'), timeout=Timeout(10.0), verify=True, cert=None, headers={'Custom-Header': 'value'}, proxies={'http://': 'http://localhost:8000'}, http2=False, cookies={'session_id': 'abc123'}, params={'key': 'value'})
