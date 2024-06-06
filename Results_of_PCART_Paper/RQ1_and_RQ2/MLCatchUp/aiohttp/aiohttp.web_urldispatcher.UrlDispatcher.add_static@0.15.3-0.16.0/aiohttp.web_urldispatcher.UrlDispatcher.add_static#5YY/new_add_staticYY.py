from aiohttp import web
app = web.Application()
app.router.add_static('/static/', path='/home/zhang/aiohttp', chunk_size=262144)
