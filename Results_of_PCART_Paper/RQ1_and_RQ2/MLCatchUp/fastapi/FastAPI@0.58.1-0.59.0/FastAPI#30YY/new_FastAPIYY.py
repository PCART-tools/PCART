from fastapi import FastAPI
from starlette.responses import JSONResponse
from starlette.routing import Route
from starlette.middleware import Middleware
app = FastAPI(default_response_class=JSONResponse, debug=True, docs_url='/docs', routes=[Route('/', endpoint=(lambda : {'Hello': 'World'}))], version='1.0.0', redoc_url='/redoc', servers=None, openapi_tags=None, openapi_url='/openapi.json', description='A simple FastAPI application example', title='My FastAPI Application', root_path_in_servers=True)
