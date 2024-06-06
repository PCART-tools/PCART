from fastapi import FastAPI
from starlette.responses import JSONResponse
from starlette.routing import Route
from starlette.middleware import Middleware
app = FastAPI(description='A simple FastAPI application example', openapi_tags=None, title='My FastAPI Application', routes=[Route('/', endpoint=(lambda : {'Hello': 'World'}))], debug=True, version='1.0.0', openapi_url='/openapi.json', root_path_in_servers=True)
