from aiohttp import web
app = web.Application()
app.router.add_static(prefix='/static/', name='static', path='/home/zhang/aiohttp', expect_handler=None, chunk_size=262144)
