from fastapi import FastAPI
from starlette.responses import JSONResponse
from starlette.routing import Route
from starlette.middleware import Middleware
app = FastAPI(routes=[Route('/', endpoint=(lambda : {'Hello': 'World'}))], servers=None, redoc_url='/redoc', default_response_class=JSONResponse, title='My FastAPI Application', version='1.0.0', openapi_tags=None, swagger_ui_oauth2_redirect_url='/docs/oauth2-redirect', middleware=None, openapi_url='/openapi.json', docs_url='/docs', swagger_ui_init_oauth=None, debug=True, description='A simple FastAPI application example', root_path_in_servers=True)
