import httpx
from httpx import Auth, Timeout, PoolLimits, URL
client = httpx.AsyncClient(headers={'Custom-Header': 'value'}, params={'key': 'value'}, auth=httpx.BasicAuth('username', 'password'))
