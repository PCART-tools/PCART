import httpx
from httpx import Auth, Timeout, PoolLimits, URL
client = httpx.AsyncClient(auth=httpx.BasicAuth('username', 'password'), max_redirects=5, app=None, headers={'Custom-Header': 'value'}, verify=True, backend='auto', http2=False, proxies={'http://': 'http://localhost:8000'}, pool_limits=PoolLimits(), base_url=URL('https://www.example.com'), dispatch=None, cert=None, timeout=Timeout(10.0), params={'key': 'value'}, cookies={'session_id': 'abc123'})
