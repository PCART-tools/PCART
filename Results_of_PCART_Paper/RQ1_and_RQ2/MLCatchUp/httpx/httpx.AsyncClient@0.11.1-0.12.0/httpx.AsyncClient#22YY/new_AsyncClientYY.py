import httpx
from httpx import Auth, Timeout, PoolLimits, URL
client = httpx.AsyncClient(params={'key': 'value'}, cookies={'session_id': 'abc123'}, headers={'Custom-Header': 'value'}, auth=httpx.BasicAuth('username', 'password'), verify=True)
