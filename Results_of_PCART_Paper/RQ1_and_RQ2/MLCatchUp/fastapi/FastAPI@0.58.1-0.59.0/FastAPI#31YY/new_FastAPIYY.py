from fastapi import FastAPI
from starlette.responses import JSONResponse
from starlette.routing import Route
from starlette.middleware import Middleware
app = FastAPI(title='My FastAPI Application', docs_url='/docs', routes=[Route('/', endpoint=(lambda : {'Hello': 'World'}))], openapi_tags=None, servers=None, version='1.0.0', openapi_url='/openapi.json', default_response_class=JSONResponse, debug=True, redoc_url='/redoc', swagger_ui_oauth2_redirect_url='/docs/oauth2-redirect', description='A simple FastAPI application example', root_path_in_servers=True)
