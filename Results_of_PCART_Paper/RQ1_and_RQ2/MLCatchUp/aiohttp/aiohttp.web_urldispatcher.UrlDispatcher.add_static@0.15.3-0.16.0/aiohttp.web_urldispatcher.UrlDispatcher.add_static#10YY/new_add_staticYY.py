from aiohttp import web
app = web.Application()
app.router.add_static(path='/home/zhang/aiohttp', prefix='/static/', name='static', chunk_size=262144)
