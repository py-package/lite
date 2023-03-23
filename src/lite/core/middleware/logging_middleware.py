import logging
from ..request import Request
from ..response import Response
from . import Middleware

class LoggingMiddleware(Middleware):
    def __call__(self):
        # Log request information
        # logging.info(f"Request: {environ['REQUEST_METHOD']} {environ['PATH_INFO']}")
        
        pass
    