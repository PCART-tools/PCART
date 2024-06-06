import aiohttp
import asyncio

async def fetch(session, url):
    async with session.get(url, ssl=None) as response:
        return (await response.text(ssl=None))

async def main():
    connector = aiohttp.TCPConnector(use_dns_cache=True, keepalive_timeout=30, limit=100, force_close=False, ttl_dns_cache=10, verify_ssl=True, local_addr=None, fingerprint=None, family=0, limit_per_host=0, resolver=None, ssl_context=None, resolve=object(), ssl=None)
    async with aiohttp.ClientSession(connector=connector, ssl=None) as session:
        html = (await fetch(session, 'http://httpbin.org/get', ssl=None))
        print(html, ssl=None)
loop = asyncio.get_event_loop()
loop.run_until_complete(main(), ssl=None)
