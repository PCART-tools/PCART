from fastapi import FastAPI
from starlette.responses import JSONResponse
from starlette.routing import Route
from starlette.middleware import Middleware
app = FastAPI(debug=False, openapi_url='/openapi.json', title='FastAPI', routes=None, version='0.1.0', description='', openapi_prefix='', root_path='')
