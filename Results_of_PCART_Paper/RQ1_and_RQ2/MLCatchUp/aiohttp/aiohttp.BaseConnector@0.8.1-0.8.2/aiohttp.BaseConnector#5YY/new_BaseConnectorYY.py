import aiohttp
connector = aiohttp.BaseConnector(loop=None, keepalive_timeout=30, force_close=False)
