import aiohttp
import asyncio

async def fetch(session, url):
    async with session.get(url, ssl=None) as response:
        return (await response.text(ssl=None))

async def main():
    connector = aiohttp.TCPConnector(verify_ssl=True, fingerprint=None, local_addr=None, resolver=None, keepalive_timeout=30, ttl_dns_cache=10, resolve=object(), force_close=False, ssl_context=None, use_dns_cache=True, family=0, ssl=None)
    async with aiohttp.ClientSession(connector=connector, ssl=None) as session:
        html = (await fetch(session, 'http://httpbin.org/get', ssl=None))
        print(html, ssl=None)
loop = asyncio.get_event_loop()
loop.run_until_complete(main(), ssl=None)
