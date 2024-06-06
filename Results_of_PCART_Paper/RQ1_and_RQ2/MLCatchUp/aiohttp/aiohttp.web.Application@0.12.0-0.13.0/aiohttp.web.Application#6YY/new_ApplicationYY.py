import aiohttp
from aiohttp import web
import logging
app = web.Application(loop=None, logger=logging.getLogger(__name__), middlewares=())
