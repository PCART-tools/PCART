import httpx
from httpx import Auth, Timeout, PoolLimits, URL
client = httpx.AsyncClient(timeout=Timeout(10.0))
