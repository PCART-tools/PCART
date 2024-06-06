import aiohttp
connector = aiohttp.BaseConnector(share_cookies=False, conn_timeout=None, force_close=False, keepalive_timeout=30, limit=None)
