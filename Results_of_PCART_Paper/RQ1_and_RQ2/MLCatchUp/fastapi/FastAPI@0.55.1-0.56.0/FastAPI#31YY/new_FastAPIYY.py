from fastapi import FastAPI
from starlette.responses import JSONResponse
from starlette.routing import Route
from starlette.middleware import Middleware
app = FastAPI(openapi_url='/openapi.json', debug=False, on_startup=None, description='', swagger_ui_init_oauth=None, version='0.1.0', docs_url='/docs', middleware=None, default_response_class=JSONResponse, routes=None, title='FastAPI', exception_handlers=None, redoc_url='/redoc', openapi_prefix='', swagger_ui_oauth2_redirect_url='/docs/oauth2-redirect', root_path='')
