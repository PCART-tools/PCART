import aiohttp
from aiohttp import web
import logging
app = web.Application(logger=logging.getLogger(__name__), middlewares=())
