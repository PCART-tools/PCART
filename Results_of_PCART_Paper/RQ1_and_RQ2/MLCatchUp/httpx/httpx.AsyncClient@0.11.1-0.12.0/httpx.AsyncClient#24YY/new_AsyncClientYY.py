import httpx
from httpx import Auth, Timeout, PoolLimits, URL
client = httpx.AsyncClient(cookies={'session_id': 'abc123'}, verify=True, auth=httpx.BasicAuth('username', 'password'), cert=None, headers={'Custom-Header': 'value'}, http2=False, params={'key': 'value'})
