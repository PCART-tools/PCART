import aiohttp
connector = aiohttp.BaseConnector(reuse_timeout=30, keepalive_timeout=30, force_close=False)
