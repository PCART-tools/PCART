from fastapi import FastAPI
from starlette.responses import JSONResponse
from starlette.routing import Route
from starlette.middleware import Middleware
app = FastAPI(routes=[Route('/', endpoint=(lambda : {'Hello': 'World'}))], redoc_url='/redoc', debug=True, middleware=None, openapi_tags=None, docs_url='/docs', version='1.0.0', exception_handlers=None, openapi_url='/openapi.json', servers=None, description='A simple FastAPI application example', title='My FastAPI Application', swagger_ui_init_oauth=None, default_response_class=JSONResponse, swagger_ui_oauth2_redirect_url='/docs/oauth2-redirect', root_path_in_servers=True)
