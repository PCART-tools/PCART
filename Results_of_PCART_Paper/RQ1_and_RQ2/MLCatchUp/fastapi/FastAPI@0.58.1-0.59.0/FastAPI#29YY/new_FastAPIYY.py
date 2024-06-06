from fastapi import FastAPI
from starlette.responses import JSONResponse
from starlette.routing import Route
from starlette.middleware import Middleware
app = FastAPI(debug=True, servers=None, version='1.0.0', openapi_url='/openapi.json', description='A simple FastAPI application example', title='My FastAPI Application', routes=[Route('/', endpoint=(lambda : {'Hello': 'World'}))], openapi_tags=None, docs_url='/docs', default_response_class=JSONResponse, root_path_in_servers=True)
