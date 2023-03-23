from .core.controller import Controller
from .core.lite import Lite
from .core.request import Request
from .core.response import Response
from .core.router import Router


class HomeController(Controller):
    def home(request, response):
        return response.html("<h1>Home Page</h1>")

    def about(request: Request, response: Response):
        # return response.html("<h1>About</h1>")
        return response.view(
            "about.html",
            {"title": "About", "contacts": ["Contact 1", "Contact 2", "Contact 3"]},
        )

    def blogs(request, response):
        return response.json(
            {
                "blogs": [
                    {"title": "Blog 1", "content": "Blog 1 content"},
                    {"title": "Blog 2", "content": "Blog 2 content"},
                    {"title": "Blog 3", "content": "Blog 3 content"},
                    {"title": "Blog 4", "content": "Blog 4 content"},
                ]
            }
        )

    def blog(request: Request, response, id):
        return response.json(
            {
                "blog": {
                    "id": id,
                    "title": "Single Blog",
                    "content": "This is single blog content",
                }
            }
        )

    def hello(request: Request, response: Response, id):
        return response.json(
            {
                # 'queries': request.query(),
                # "inputs": request.only("foo", "contact.address.zone"),
                # 'session':
                "blog": {"id": id, "title": "Hello", "content": "Hello content"}
            }
        )


router = Router()
router.get("/", HomeController.home)
router.get("/about", HomeController.about)
router.get("/blogs", HomeController.blogs)
router.get("/blogs/:id", HomeController.blog)
router.post("/blogs/:id/hello", HomeController.hello)
router.get("/ping", lambda request, response: response.text("pong"))

app = Lite(router)
