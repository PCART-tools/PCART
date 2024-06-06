import httpx
from httpx import Auth, Timeout, PoolLimits, URL
client = httpx.AsyncClient(trust_env=True, max_redirects=5, headers={'Custom-Header': 'value'}, verify=True, cert=None, pool_limits=PoolLimits(), backend='auto', auth=httpx.BasicAuth('username', 'password'), params={'key': 'value'}, app=None, timeout=Timeout(10.0), base_url=URL('https://www.example.com'), cookies={'session_id': 'abc123'}, http2=False, dispatch=None, proxies={'http://': 'http://localhost:8000'})
