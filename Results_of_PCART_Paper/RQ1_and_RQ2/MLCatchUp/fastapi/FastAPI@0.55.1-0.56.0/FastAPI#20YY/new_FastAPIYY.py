from fastapi import FastAPI
from starlette.responses import JSONResponse
from starlette.routing import Route
from starlette.middleware import Middleware
app = FastAPI(title='FastAPI', debug=False, description='', routes=None, root_path='')
