import httpx
from httpx import Auth, Timeout, PoolLimits, URL
client = httpx.AsyncClient(base_url=URL('https://www.example.com'))
