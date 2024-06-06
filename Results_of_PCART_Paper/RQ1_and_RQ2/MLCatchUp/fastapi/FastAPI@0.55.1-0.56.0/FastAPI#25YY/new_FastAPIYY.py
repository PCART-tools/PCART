from fastapi import FastAPI
from starlette.responses import JSONResponse
from starlette.routing import Route
from starlette.middleware import Middleware
app = FastAPI(openapi_url='/openapi.json', default_response_class=JSONResponse, version='0.1.0', routes=None, description='', debug=False, openapi_prefix='', title='FastAPI', docs_url='/docs', root_path='')
