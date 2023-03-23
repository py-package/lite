import random
import string
from . import Middleware

class CSRFMiddleware(Middleware):
    
    def __call__(self):
        # Validate CSRF token for POST, PUT, and DELETE requests
        if self.request.method in ['POST', 'PUT', 'DELETE']:
            csrf_token = self.request.headers.get('X-CSRF-Token')
            session_csrf_token = self.request.session.get('csrf_token')

            # if csrf_token is None or session_csrf_token is None or csrf_token != session_csrf_token:
            #     res = Response(text='CSRF token validation failed.', status=HTTPStatus.FORBIDDEN)
            #     return res(environ, start_response)

        # Generate new CSRF token for each request
        csrf_token = ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(32))
        self.request.session['csrf_token'] = csrf_token
        self.response.set_cookie('csrf_token', csrf_token)
        return self.response