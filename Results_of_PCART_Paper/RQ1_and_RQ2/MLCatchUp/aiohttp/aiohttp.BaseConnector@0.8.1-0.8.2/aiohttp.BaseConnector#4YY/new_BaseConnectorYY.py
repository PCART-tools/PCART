import aiohttp
connector = aiohttp.BaseConnector(share_cookies=False, keepalive_timeout=30, force_close=False)
