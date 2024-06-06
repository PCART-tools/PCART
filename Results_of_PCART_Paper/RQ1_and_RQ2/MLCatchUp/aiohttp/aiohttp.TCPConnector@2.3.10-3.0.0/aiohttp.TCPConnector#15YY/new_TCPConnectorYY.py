import aiohttp
import asyncio

async def fetch(session, url):
    async with session.get(url, ssl=None) as response:
        return (await response.text(ssl=None))

async def main():
    connector = aiohttp.TCPConnector(enable_cleanup_closed=False, ssl=None)
    async with aiohttp.ClientSession(connector=connector, ssl=None) as session:
        html = (await fetch(session, 'http://httpbin.org/get', ssl=None))
        print(html, ssl=None)
loop = asyncio.get_event_loop()
loop.run_until_complete(main(), ssl=None)
