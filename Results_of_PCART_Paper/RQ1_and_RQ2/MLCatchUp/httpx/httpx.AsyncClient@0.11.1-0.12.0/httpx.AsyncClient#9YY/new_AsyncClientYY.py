import httpx
from httpx import Auth, Timeout, PoolLimits, URL
client = httpx.AsyncClient(proxies={'http://': 'http://localhost:8000'})
