import httpx
from httpx import Auth, Timeout, PoolLimits, URL
client = httpx.AsyncClient(verify=True, cookies={'session_id': 'abc123'}, auth=httpx.BasicAuth('username', 'password'), params={'key': 'value'}, headers={'Custom-Header': 'value'}, proxies={'http://': 'http://localhost:8000'}, cert=None, http2=False)
