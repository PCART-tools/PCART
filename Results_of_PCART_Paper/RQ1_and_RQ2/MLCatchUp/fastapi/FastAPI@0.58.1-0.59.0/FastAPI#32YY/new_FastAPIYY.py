from fastapi import FastAPI
from starlette.responses import JSONResponse
from starlette.routing import Route
from starlette.middleware import Middleware
app = FastAPI(docs_url='/docs', swagger_ui_init_oauth=None, default_response_class=JSONResponse, openapi_url='/openapi.json', routes=[Route('/', endpoint=(lambda : {'Hello': 'World'}))], version='1.0.0', swagger_ui_oauth2_redirect_url='/docs/oauth2-redirect', servers=None, title='My FastAPI Application', redoc_url='/redoc', description='A simple FastAPI application example', openapi_tags=None, debug=True, root_path_in_servers=True)
