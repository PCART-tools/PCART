import httpx
from httpx import Auth, Timeout, PoolLimits, URL
client = httpx.AsyncClient(trust_env=True)
