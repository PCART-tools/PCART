from fastapi import FastAPI
from starlette.responses import JSONResponse
from starlette.routing import Route
from starlette.middleware import Middleware
app = FastAPI(openapi_url='/openapi.json', default_response_class=JSONResponse, description='', swagger_ui_oauth2_redirect_url='/docs/oauth2-redirect', openapi_prefix='', debug=False, docs_url='/docs', middleware=None, version='0.1.0', redoc_url='/redoc', routes=None, title='FastAPI', swagger_ui_init_oauth=None, root_path='')
