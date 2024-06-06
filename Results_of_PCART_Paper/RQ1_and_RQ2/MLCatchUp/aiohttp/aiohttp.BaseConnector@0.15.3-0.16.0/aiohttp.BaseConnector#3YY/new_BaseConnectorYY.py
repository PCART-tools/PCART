import aiohttp
connector = aiohttp.BaseConnector(keepalive_timeout=30, limit=None)
