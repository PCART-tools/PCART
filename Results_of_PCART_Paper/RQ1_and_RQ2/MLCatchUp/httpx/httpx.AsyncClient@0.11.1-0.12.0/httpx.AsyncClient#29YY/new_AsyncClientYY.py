import httpx
from httpx import Auth, Timeout, PoolLimits, URL
client = httpx.AsyncClient(base_url=URL('https://www.example.com'), max_redirects=5, proxies={'http://': 'http://localhost:8000'}, headers={'Custom-Header': 'value'}, pool_limits=PoolLimits(), params={'key': 'value'}, timeout=Timeout(10.0), cert=None, verify=True, http2=False, auth=httpx.BasicAuth('username', 'password'), cookies={'session_id': 'abc123'})
