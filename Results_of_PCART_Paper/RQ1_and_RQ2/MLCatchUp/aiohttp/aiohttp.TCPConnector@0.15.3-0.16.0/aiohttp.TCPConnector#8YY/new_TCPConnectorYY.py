import aiohttp
import socket
connector = aiohttp.TCPConnector(resolve=False, verify_ssl=True, ssl_context=None, family=socket.AF_INET, fingerprint=None)
