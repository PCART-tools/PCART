import httpx
from httpx import Auth, Timeout, PoolLimits, URL
client = httpx.AsyncClient(params={'key': 'value'}, max_redirects=5, headers={'Custom-Header': 'value'}, app=None, auth=httpx.BasicAuth('username', 'password'), verify=True, timeout=Timeout(10.0), dispatch=None, proxies={'http://': 'http://localhost:8000'}, pool_limits=PoolLimits(), base_url=URL('https://www.example.com'), http2=False, cert=None, cookies={'session_id': 'abc123'})
