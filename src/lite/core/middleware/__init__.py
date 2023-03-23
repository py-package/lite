from ..request import Request
from ..response import Response

class Middleware:
    def __init__(self, req: Request, res: Response):
        self.request = req
        self.response = res

    def __call__(self):
        pass