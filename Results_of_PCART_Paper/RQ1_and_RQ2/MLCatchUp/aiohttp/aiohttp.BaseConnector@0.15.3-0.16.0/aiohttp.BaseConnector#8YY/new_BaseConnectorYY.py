import aiohttp
connector = aiohttp.BaseConnector(keepalive_timeout=30, share_cookies=False, conn_timeout=None, limit=None)
