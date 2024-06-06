import httpx
from httpx import Auth, Timeout, PoolLimits, URL
client = httpx.AsyncClient(max_redirects=5, app=None, http2=False, backend='auto', trust_env=True, uds=None, dispatch=None, pool_limits=PoolLimits(), base_url=URL('https://www.example.com'), proxies={'http://': 'http://localhost:8000'}, cookies={'session_id': 'abc123'}, headers={'Custom-Header': 'value'}, timeout=Timeout(10.0), params={'key': 'value'}, cert=None, auth=httpx.BasicAuth('username', 'password'), verify=True)
