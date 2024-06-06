import httpx
from httpx import Auth, Timeout, PoolLimits, URL
client = httpx.AsyncClient(cookies={'session_id': 'abc123'})
