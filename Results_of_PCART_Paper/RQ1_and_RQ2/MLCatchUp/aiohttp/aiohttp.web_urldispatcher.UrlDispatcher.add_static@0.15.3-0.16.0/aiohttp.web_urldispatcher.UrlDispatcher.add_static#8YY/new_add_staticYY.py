from aiohttp import web
app = web.Application()
app.router.add_static('/static/', expect_handler=None, path='/home/zhang/aiohttp', name='static', chunk_size=262144)
