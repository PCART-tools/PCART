from fastapi import FastAPI
from starlette.responses import JSONResponse
from starlette.routing import Route
from starlette.middleware import Middleware
app = FastAPI(middleware=None, routes=None, title='FastAPI', version='0.1.0', debug=False, swagger_ui_oauth2_redirect_url='/docs/oauth2-redirect', openapi_prefix='', description='', redoc_url='/redoc', default_response_class=JSONResponse, swagger_ui_init_oauth=None, openapi_url='/openapi.json', docs_url='/docs', exception_handlers=None, root_path='')
