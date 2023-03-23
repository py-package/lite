from waitress import serve

from .router import Router


class Lite:
    def __init__(
        self, router: Router, host: str = "127.0.0.1", port: int = 8080, threads=1
    ):
        self.host = host
        self.port = port
        self.router = router
        self.threads = threads

    def start(self):
        print(f"Starting server on {self.host}:{self.port}")
        serve(
            self.create_request_handler(),
            host=self.host,
            port=self.port,
            threads=self.threads,
        )

    def create_request_handler(self):

        router = self.router

        class RequestHandler:
            def __init__(self, environ, start_response):
                self.environ = environ
                self.start_response = start_response

            def __iter__(self):
                from .request import Request
                from .response import Response

                req = Request(self.environ)
                res = Response()

                handler, path_params = router.get_handler(req.path, req.method)
                if handler:
                    response_body = handler(req, res, **path_params)
                    status = f"{res.status_code} {res.reason_phrase}"
                    headers = list(res.headers.items())
                else:
                    status = "404 Not Found"
                    response_body = res.view("404.html", status=status)
                    headers = [("Content-Type", res.content_type)]

                self.start_response(status, headers)
                return iter(response_body)

        return RequestHandler