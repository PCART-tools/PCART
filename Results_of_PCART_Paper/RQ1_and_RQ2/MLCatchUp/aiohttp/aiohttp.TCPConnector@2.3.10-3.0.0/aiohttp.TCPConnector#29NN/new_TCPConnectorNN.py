import aiohttp
import asyncio

async def fetch(session, url):
    async with session.get(url, ssl=None) as response:
        return (await response.text(ssl=None))

async def main():
    connector = aiohttp.TCPConnector(enable_cleanup_closed=False, keepalive_timeout=30, fingerprint=None, verify_ssl=True, ttl_dns_cache=10, limit=100, use_dns_cache=True, resolve=object(), ssl_context=None, local_addr=None, force_close=False, limit_per_host=0, resolver=None, family=0, ssl=None)
    async with aiohttp.ClientSession(connector=connector, ssl=None) as session:
        html = (await fetch(session, 'http://httpbin.org/get', ssl=None))
        print(html, ssl=None)
loop = asyncio.get_event_loop()
loop.run_until_complete(main(), ssl=None)
