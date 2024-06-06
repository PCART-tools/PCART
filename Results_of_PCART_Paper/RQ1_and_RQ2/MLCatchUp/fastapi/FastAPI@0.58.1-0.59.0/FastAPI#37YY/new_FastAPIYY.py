from fastapi import FastAPI
from starlette.responses import JSONResponse
from starlette.routing import Route
from starlette.middleware import Middleware
app = FastAPI(servers=None, openapi_prefix='', swagger_ui_oauth2_redirect_url='/docs/oauth2-redirect', default_response_class=JSONResponse, debug=True, openapi_url='/openapi.json', title='My FastAPI Application', description='A simple FastAPI application example', exception_handlers=None, routes=[Route('/', endpoint=(lambda : {'Hello': 'World'}))], openapi_tags=None, redoc_url='/redoc', swagger_ui_init_oauth=None, on_shutdown=None, version='1.0.0', middleware=None, docs_url='/docs', on_startup=None, root_path_in_servers=True)
