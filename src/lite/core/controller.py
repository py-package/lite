from http import HTTPStatus


class Controller:
    request = None
    response = None

    @classmethod
    def set_request(cls, request):
        cls.request = request

    @classmethod
    def set_response(cls, response):
        cls.response = response

    @classmethod
    def get(cls):
        cls.response.status = HTTPStatus.NOT_IMPLEMENTED

    @classmethod
    def post(cls):
        cls.response.status = HTTPStatus.NOT_IMPLEMENTED

    @classmethod
    def put(cls):
        cls.response.status = HTTPStatus.NOT_IMPLEMENTED

    @classmethod
    def patch(cls):
        cls.response.status = HTTPStatus.NOT_IMPLEMENTED

    @classmethod
    def delete(cls):
        cls.response.status = HTTPStatus.NOT_IMPLEMENTED
