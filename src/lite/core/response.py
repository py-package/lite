import json
from xml.etree.ElementTree import Element, tostring

class Response:
    def __init__(self, handler):
        self.handler = handler
        self.content_type = 'text/plain'
        self.headers = []

    def start_response(self, status, headers=None):
        if headers is None:
            headers = []
        headers.append(('Content-Type', self.content_type))
        self.handler.send_response(int(status.split()[0]))
        for header, value in headers:
            self.handler.send_header(header, value)
        self.handler.end_headers()

    def _format_json(self, data):
        """
        Recursively convert all FileStorage objects to their filenames
        """
        for key, value in data.items():
            if hasattr(value, 'filename'):
                data[key] = value.filename
            elif isinstance(value, dict):
                self._format_json(value)
        return data

    def json(self, data, status='200 OK'):
        """
        Return a JSON response
        """
        self.content_type = 'application/json'
        data = self._format_json(data)
        response_body = json.dumps(data).encode('utf-8')
        self.start_response(status)
        return [response_body]

    def xml(self, root_element, status='200 OK'):
        """
        Return an XML response
        """
        self.content_type = 'application/xml'
        response_body = tostring(root_element, encoding='utf-8')
        self.start_response(status)
        return [response_body]

    def html(self, html_string, status='200 OK'):
        """
        Return an HTML response
        """
        self.content_type = 'text/html'
        response_body = html_string.encode('utf-8')
        self.start_response(status)
        return [response_body]

    def template(self, template_path, context=None, status='200 OK'):
        """
        Return a rendered template
        """
        if context is None:
            context = {}
        self.content_type = 'text/html'
        response_body = self.render_template(template_path, context).encode('utf-8')
        self.start_response(status)
        return [response_body]

    def render_template(self, template_path, context):
        """
        Render a template using Jinja2
        """
        from jinja2 import Environment, FileSystemLoader

        env = Environment(loader=FileSystemLoader(searchpath='./templates'))
        template = env.get_template(template_path)
        return template.render(context)
    
    def text(self, text_string, status='200 OK'):
        """
        Return a plain text response
        """
        self.content_type = 'text/plain'
        response_body = text_string.encode('utf-8')
        self.start_response(status)
        return [response_body]
