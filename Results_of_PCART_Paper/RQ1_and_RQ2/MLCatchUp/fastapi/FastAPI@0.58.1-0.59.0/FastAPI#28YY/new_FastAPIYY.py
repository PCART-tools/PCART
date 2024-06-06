from fastapi import FastAPI
from starlette.responses import JSONResponse
from starlette.routing import Route
from starlette.middleware import Middleware
app = FastAPI(debug=True, title='My FastAPI Application', openapi_tags=None, version='1.0.0', servers=None, openapi_url='/openapi.json', default_response_class=JSONResponse, routes=[Route('/', endpoint=(lambda : {'Hello': 'World'}))], description='A simple FastAPI application example', root_path_in_servers=True)
