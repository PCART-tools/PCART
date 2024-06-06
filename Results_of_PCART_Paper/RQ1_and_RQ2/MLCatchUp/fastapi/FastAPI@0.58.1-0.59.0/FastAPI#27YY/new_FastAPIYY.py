from fastapi import FastAPI
from starlette.responses import JSONResponse
from starlette.routing import Route
from starlette.middleware import Middleware
app = FastAPI(routes=[Route('/', endpoint=(lambda : {'Hello': 'World'}))], version='1.0.0', openapi_tags=None, description='A simple FastAPI application example', servers=None, openapi_url='/openapi.json', title='My FastAPI Application', debug=True, root_path_in_servers=True)
