import aiohttp
connector = aiohttp.BaseConnector(loop=None, force_close=False, keepalive_timeout=30, share_cookies=False, conn_timeout=None, limit=None)
