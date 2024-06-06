import httpx
from httpx import Auth, Timeout, PoolLimits, URL
client = httpx.AsyncClient(http2=False)
