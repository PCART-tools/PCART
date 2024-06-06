import aiohttp
import asyncio

async def fetch_page(url, loop):
    connector = aiohttp.TCPConnector(resolve=False, verify_ssl=True, ssl_context=None)
    response = await aiohttp.request('GET', url, connector=connector)
    raw_response = await response.read()
loop = asyncio.get_event_loop()
loop.run_until_complete(fetch_page('http://example.com', loop))
