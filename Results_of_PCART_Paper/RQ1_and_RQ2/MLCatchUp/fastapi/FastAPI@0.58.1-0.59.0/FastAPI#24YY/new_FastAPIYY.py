from fastapi import FastAPI
from starlette.responses import JSONResponse
from starlette.routing import Route
from starlette.middleware import Middleware
app = FastAPI(version='1.0.0', routes=[Route('/', endpoint=(lambda : {'Hello': 'World'}))], title='My FastAPI Application', debug=True, description='A simple FastAPI application example', root_path_in_servers=True)
