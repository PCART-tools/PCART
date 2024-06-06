import aiohttp
import socket
connector = aiohttp.TCPConnector(resolve=False, verify_ssl=True, fingerprint=None)
