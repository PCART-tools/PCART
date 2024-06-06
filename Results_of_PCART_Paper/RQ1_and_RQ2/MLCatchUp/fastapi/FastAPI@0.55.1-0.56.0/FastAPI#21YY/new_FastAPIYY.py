from fastapi import FastAPI
from starlette.responses import JSONResponse
from starlette.routing import Route
from starlette.middleware import Middleware
app = FastAPI(title='FastAPI', description='', routes=None, version='0.1.0', debug=False, root_path='')
