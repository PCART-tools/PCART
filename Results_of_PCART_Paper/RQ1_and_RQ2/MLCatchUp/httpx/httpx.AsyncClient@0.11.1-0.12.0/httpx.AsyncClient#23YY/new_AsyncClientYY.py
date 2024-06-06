import httpx
from httpx import Auth, Timeout, PoolLimits, URL
client = httpx.AsyncClient(verify=True, cookies={'session_id': 'abc123'}, cert=None, headers={'Custom-Header': 'value'}, auth=httpx.BasicAuth('username', 'password'), params={'key': 'value'})
