from fastapi import FastAPI
from starlette.responses import JSONResponse
from starlette.routing import Route
from starlette.middleware import Middleware
app = FastAPI(swagger_ui_oauth2_redirect_url='/docs/oauth2-redirect', root_path='')
