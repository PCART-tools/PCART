from fastapi import FastAPI
from starlette.responses import JSONResponse
from starlette.routing import Route
from starlette.middleware import Middleware
app = FastAPI(routes=None, redoc_url='/redoc', openapi_prefix='', swagger_ui_init_oauth=None, openapi_url='/openapi.json', version='0.1.0', default_response_class=JSONResponse, description='', swagger_ui_oauth2_redirect_url='/docs/oauth2-redirect', docs_url='/docs', debug=False, title='FastAPI', root_path='')
