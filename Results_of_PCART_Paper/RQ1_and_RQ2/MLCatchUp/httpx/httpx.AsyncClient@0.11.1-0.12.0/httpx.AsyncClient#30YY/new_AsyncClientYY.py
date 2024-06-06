import httpx
from httpx import Auth, Timeout, PoolLimits, URL
client = httpx.AsyncClient(headers={'Custom-Header': 'value'}, max_redirects=5, timeout=Timeout(10.0), dispatch=None, params={'key': 'value'}, cookies={'session_id': 'abc123'}, base_url=URL('https://www.example.com'), proxies={'http://': 'http://localhost:8000'}, http2=False, pool_limits=PoolLimits(), verify=True, auth=httpx.BasicAuth('username', 'password'), cert=None)
