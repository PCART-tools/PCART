from fastapi import FastAPI
from starlette.responses import JSONResponse
from starlette.routing import Route
from starlette.middleware import Middleware
app = FastAPI(docs_url='/docs', title='FastAPI', version='0.1.0', redoc_url='/redoc', openapi_url='/openapi.json', debug=False, routes=None, openapi_prefix='', default_response_class=JSONResponse, description='', root_path='')
