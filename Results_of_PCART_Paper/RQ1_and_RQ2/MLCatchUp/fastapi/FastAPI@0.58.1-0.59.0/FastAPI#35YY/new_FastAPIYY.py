from fastapi import FastAPI
from starlette.responses import JSONResponse
from starlette.routing import Route
from starlette.middleware import Middleware
app = FastAPI(openapi_tags=None, default_response_class=JSONResponse, docs_url='/docs', openapi_url='/openapi.json', routes=[Route('/', endpoint=(lambda : {'Hello': 'World'}))], redoc_url='/redoc', exception_handlers=None, servers=None, middleware=None, description='A simple FastAPI application example', swagger_ui_init_oauth=None, swagger_ui_oauth2_redirect_url='/docs/oauth2-redirect', title='My FastAPI Application', debug=True, version='1.0.0', on_startup=None, root_path_in_servers=True)
