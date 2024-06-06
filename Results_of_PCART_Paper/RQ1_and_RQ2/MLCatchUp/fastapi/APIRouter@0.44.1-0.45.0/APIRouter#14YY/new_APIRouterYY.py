from fastapi import FastAPI, APIRouter
from fastapi.routing import APIRoute
from starlette.routing import Route

def example_endpoint():
    return {'message': 'Hello'}
router = APIRouter([Route('/', endpoint=example_endpoint)], redirect_slashes=True, default=None, dependency_overrides_provider=None, default_response_class=None)
