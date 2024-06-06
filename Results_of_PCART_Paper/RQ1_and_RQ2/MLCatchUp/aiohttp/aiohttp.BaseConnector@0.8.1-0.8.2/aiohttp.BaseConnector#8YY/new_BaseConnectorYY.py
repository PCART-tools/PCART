import aiohttp
connector = aiohttp.BaseConnector(share_cookies=False, conn_timeout=None, reuse_timeout=30, loop=None, keepalive_timeout=30, force_close=False)
