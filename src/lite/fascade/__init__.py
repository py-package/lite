
def view(template, context=None):
    from ..core.view import View
    return View().render(template, context=context)