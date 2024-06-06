from fastapi import FastAPI
from starlette.responses import JSONResponse
from starlette.routing import Route
from starlette.middleware import Middleware
app = FastAPI(redoc_url='/redoc', version='0.1.0', openapi_url='/openapi.json', debug=False, default_response_class=JSONResponse, routes=None, swagger_ui_oauth2_redirect_url='/docs/oauth2-redirect', openapi_prefix='', title='FastAPI', docs_url='/docs', description='', root_path='')
