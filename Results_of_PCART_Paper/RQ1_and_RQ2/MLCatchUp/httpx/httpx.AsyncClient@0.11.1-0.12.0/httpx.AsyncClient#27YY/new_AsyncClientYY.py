import httpx
from httpx import Auth, Timeout, PoolLimits, URL
client = httpx.AsyncClient(http2=False, proxies={'http://': 'http://localhost:8000'}, auth=httpx.BasicAuth('username', 'password'), cookies={'session_id': 'abc123'}, headers={'Custom-Header': 'value'}, params={'key': 'value'}, pool_limits=PoolLimits(), verify=True, cert=None, timeout=Timeout(10.0))
