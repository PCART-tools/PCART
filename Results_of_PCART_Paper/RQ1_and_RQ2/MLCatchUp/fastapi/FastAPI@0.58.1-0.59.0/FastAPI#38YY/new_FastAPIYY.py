from fastapi import FastAPI
from starlette.responses import JSONResponse
from starlette.routing import Route
from starlette.middleware import Middleware
app = FastAPI(version='1.0.0', openapi_url='/openapi.json', debug=True, servers=None, default_response_class=JSONResponse, on_shutdown=None, swagger_ui_oauth2_redirect_url='/docs/oauth2-redirect', root_path='', description='A simple FastAPI application example', openapi_prefix='', title='My FastAPI Application', openapi_tags=None, exception_handlers=None, docs_url='/docs', middleware=None, redoc_url='/redoc', routes=[Route('/', endpoint=(lambda : {'Hello': 'World'}))], swagger_ui_init_oauth=None, on_startup=None, root_path_in_servers=True)
