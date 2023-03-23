from jinja2 import ChoiceLoader, Environment, FileSystemLoader


class View:
    def __init__(self) -> None:
        self.template_engine = Environment(
            loader=FileSystemLoader(["views/", "src/lite/templates/"]),
            trim_blocks=True,
            lstrip_blocks=True,
        )

    def render(self, template_path, context=None):
        if context is None:
            context = {}
        template = self.template_engine.get_template(template_path)
        return template.render(context)
