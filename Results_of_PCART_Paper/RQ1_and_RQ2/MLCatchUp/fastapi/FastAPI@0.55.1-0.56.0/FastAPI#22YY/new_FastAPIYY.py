from fastapi import FastAPI
from starlette.responses import JSONResponse
from starlette.routing import Route
from starlette.middleware import Middleware
app = FastAPI(openapi_url='/openapi.json', debug=False, version='0.1.0', routes=None, description='', title='FastAPI', root_path='')
