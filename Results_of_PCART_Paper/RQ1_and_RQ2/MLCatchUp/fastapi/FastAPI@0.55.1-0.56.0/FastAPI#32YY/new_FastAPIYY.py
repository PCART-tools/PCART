from fastapi import FastAPI
from starlette.responses import JSONResponse
from starlette.routing import Route
from starlette.middleware import Middleware
app = FastAPI(openapi_url='/openapi.json', redoc_url='/redoc', default_response_class=JSONResponse, on_startup=None, description='', title='FastAPI', docs_url='/docs', routes=None, swagger_ui_init_oauth=None, exception_handlers=None, swagger_ui_oauth2_redirect_url='/docs/oauth2-redirect', middleware=None, debug=False, on_shutdown=None, openapi_prefix='', version='0.1.0', root_path='')
