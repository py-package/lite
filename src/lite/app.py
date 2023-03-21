from .core.lite import Lite

def lite_app(env, start_response):
    status_code = 200
    headers = [('Content-Type', 'text/html')]
    response_body = b"Hello World!"
    status = f"{status_code} OK"
    start_response(status, headers)
    return [response_body]

app = Lite(lite_app)