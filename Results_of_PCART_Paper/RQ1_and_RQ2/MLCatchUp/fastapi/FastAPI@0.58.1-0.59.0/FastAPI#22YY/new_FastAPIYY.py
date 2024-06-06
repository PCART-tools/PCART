from fastapi import FastAPI
from starlette.responses import JSONResponse
from starlette.routing import Route
from starlette.middleware import Middleware
app = FastAPI(title='My FastAPI Application', debug=True, routes=[Route('/', endpoint=(lambda : {'Hello': 'World'}))], root_path_in_servers=True)
