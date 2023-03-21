import socket
from http.server import BaseHTTPRequestHandler, HTTPServer

class Lite:
    def __init__(self, app, host='127.0.0.1', port=8080):
        self.app = app
        self.host = host
        self.port = port

    def start(self):
        print(f'Starting server on {self.host}:{self.port}')
        server = HTTPServer((self.host, self.port), self.create_request_handler())
        server.serve_forever()

    def create_request_handler(self):
        app = self.app

        class CustomRequestHandler(BaseHTTPRequestHandler):
            def do_GET(self):
                env = self.create_environ()

                def start_response(status, headers):
                    self.send_response(int(status.split()[0]))
                    for header, value in headers:
                        self.send_header(header, value)
                    self.end_headers()

                response_body = app(env, start_response)
                self.wfile.write(b''.join(response_body))

            def create_environ(self):
                env = {
                    'REQUEST_METHOD': 'GET',
                    'PATH_INFO': self.path,
                    'SERVER_NAME': self.server.server_name,
                    'SERVER_PORT': str(self.server.server_port),
                }
                return env

        return CustomRequestHandler