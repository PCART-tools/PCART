from fastapi import FastAPI
from starlette.responses import JSONResponse
from starlette.routing import Route
from starlette.middleware import Middleware
app = FastAPI(swagger_ui_oauth2_redirect_url='/docs/oauth2-redirect', openapi_tags=None, exception_handlers=None, routes=[Route('/', endpoint=(lambda : {'Hello': 'World'}))], middleware=None, default_response_class=JSONResponse, swagger_ui_init_oauth=None, description='A simple FastAPI application example', version='1.0.0', debug=True, on_startup=None, docs_url='/docs', servers=None, redoc_url='/redoc', openapi_url='/openapi.json', title='My FastAPI Application', on_shutdown=None, root_path_in_servers=True)
