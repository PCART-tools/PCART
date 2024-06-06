from fastapi import FastAPI, APIRouter
from fastapi.routing import APIRoute
from starlette.routing import Route

def example_endpoint():
    return {'message': 'Hello'}
router = APIRouter(routes=[Route('/', endpoint=example_endpoint)], redirect_slashes=True, default=None, default_response_class=None)
