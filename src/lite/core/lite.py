import http
from http.cookies import SimpleCookie
import socket
from http.server import BaseHTTPRequestHandler, HTTPServer

class Lite:
    def __init__(self, router, host='127.0.0.1', port=8080):
        self.host = host
        self.port = port
        self.router = router

    def start(self):
        print(f'Starting server on {self.host}:{self.port}')
        server = HTTPServer((self.host, self.port), self.create_request_handler())
        server.serve_forever()

    def create_request_handler(self):
        from .request import Request
        from .response import Response
        
        router = self.router
        class RequestHandler(Request):
            def _handle_request(self):
                handler_info = router.get_handler(self.path, self.command)
                if handler_info:
                    res = Response(self)
                    handler, paths, queries = handler_info
                    self.queries.update(queries)
                    response_body = handler(self, res, **paths)
                    self.wfile.write(b''.join(response_body))
                    self.end_headers()
                else:
                    self.send_error(404, "Not Found")

            do_GET = do_POST = do_PUT = do_PATCH = do_DELETE = do_OPTIONS = _handle_request

        return RequestHandler