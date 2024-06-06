import httpx
from httpx import Auth, Timeout, PoolLimits, URL
client = httpx.AsyncClient(auth=httpx.BasicAuth('username', 'password'))
