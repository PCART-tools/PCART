import httpx
from httpx import Auth, Timeout, PoolLimits, URL
client = httpx.AsyncClient(cookies={'session_id': 'abc123'}, max_redirects=5, http2=False, timeout=Timeout(10.0), verify=True, params={'key': 'value'}, cert=None, auth=httpx.BasicAuth('username', 'password'), headers={'Custom-Header': 'value'}, proxies={'http://': 'http://localhost:8000'}, pool_limits=PoolLimits())
