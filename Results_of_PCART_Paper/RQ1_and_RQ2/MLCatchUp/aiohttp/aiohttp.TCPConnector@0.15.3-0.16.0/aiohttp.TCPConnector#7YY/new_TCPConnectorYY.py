import aiohttp
import socket
connector = aiohttp.TCPConnector(verify_ssl=True, family=socket.AF_INET, resolve=False, fingerprint=None)
