import httpx
from httpx import Request
from httpx import USE_CLIENT_DEFAULT
client = httpx.Client()
request = Request('GET', 'https://www.example.com')
client.send(stream=False, auth=USE_CLIENT_DEFAULT, allow_redirects=USE_CLIENT_DEFAULT, timeout=USE_CLIENT_DEFAULT, request=request)
