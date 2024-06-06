from fastapi import FastAPI
from starlette.responses import JSONResponse
from starlette.routing import Route
from starlette.middleware import Middleware
app = FastAPI(title='My FastAPI Application', description='A simple FastAPI application example', routes=[Route('/', endpoint=(lambda : {'Hello': 'World'}))], version='1.0.0', openapi_url='/openapi.json', debug=True, root_path_in_servers=True)
