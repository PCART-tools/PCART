import httpx
from httpx import Auth, Timeout, PoolLimits, URL
client = httpx.AsyncClient(params={'key': 'value'})
