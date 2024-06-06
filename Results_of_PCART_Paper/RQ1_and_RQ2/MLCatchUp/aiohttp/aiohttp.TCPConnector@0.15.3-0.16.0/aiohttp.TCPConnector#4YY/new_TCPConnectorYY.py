import aiohttp
import socket
connector = aiohttp.TCPConnector(family=socket.AF_INET, fingerprint=None)
