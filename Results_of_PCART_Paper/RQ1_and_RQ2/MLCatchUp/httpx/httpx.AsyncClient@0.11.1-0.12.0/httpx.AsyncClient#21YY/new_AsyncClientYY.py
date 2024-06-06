import httpx
from httpx import Auth, Timeout, PoolLimits, URL
client = httpx.AsyncClient(auth=httpx.BasicAuth('username', 'password'), cookies={'session_id': 'abc123'}, params={'key': 'value'}, headers={'Custom-Header': 'value'})
