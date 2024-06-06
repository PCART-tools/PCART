import aiohttp
from aiohttp import web
import logging
app = web.Application(handler_factory=aiohttp.web.RequestHandlerFactory, middlewares=())
