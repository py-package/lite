import cgi
import io
import json
from http.cookies import SimpleCookie
from urllib.parse import parse_qs, parse_qsl

from ..session import Session


class Request:
    queries = {}
    inputs = {}

    def __init__(self, environ):
        self.environ = environ
        self.queries = self.__get_queries(environ["QUERY_STRING"])

    def __get_queries(self, query_string: str):
        queries = {}
        if query_string:
            queries = parse_qsl(query_string)
            queries = dict(queries)
        return queries

    @property
    def method(self):
        return self.environ["REQUEST_METHOD"]

    @property
    def path(self):
        return self.environ["PATH_INFO"]

    @property
    def headers(self):
        return self.environ

    @property
    def cookies(self):
        cookie_header = self.headers.get("HTTP_COOKIE")
        cookies = {}
        if cookie_header:
            cookie = SimpleCookie(cookie_header)
            for key, morsel in cookie.items():
                cookies[key] = morsel.value
        return cookies

    def __get_session(self):
        session_id = self.cookies.get("session_id")
        if session_id:
            session = Session.load(session_id)
        else:
            session = Session()

        if session.id != session_id:
            cookie = SimpleCookie()
            cookie["session_id"] = session.id
            self.headers["Set-Cookie"] = cookie.output(header="", sep=";")

        return session

    @property
    def session(self):
        return self.__get_session()

    def query(self, key=None, value=None):
        """
        Returns the query string as a dictionary.
        If a key is provided, returns the value for that key.
        If a key is provided but not found, returns the default value.

        Example:
            request.query() # {'name': 'John Doe'}
            request.query('name') # 'John Doe'
            request.query('name', 'John Doe') # 'John Doe'
        """
        if not self.queries:
            self.queries = self._parse_query(self.path)

        if key:
            return self.queries.get(key, value)
        return self.queries

    def input(self, key=None, value=None):
        """
        Returns the request body as a dictionary.
        If a key is provided, returns the value for that key.
        If a key is provided but not found, returns the default value.
        Example:
            request.input()
            request.input('name')
        """
        body = self.get_body()
        data = self._parse_input(body)
        if key:
            return data.get(key, value)
        return data

    def only(self, *keys):
        """
        Returns a dictionary with only the specified keys.
        Example:
            request.only('name', 'email')
        """
        data = self.input()

        def extract(d, keys):
            if isinstance(d, dict):
                if isinstance(keys, str):
                    keys = keys.split(".")
                if len(keys) == 1:
                    return d.get(keys[0])
                else:
                    return extract(d.get(keys[0], {}), keys[1:])
            elif isinstance(d, list):
                return [extract(item, keys) for item in d]
            else:
                return d

        results = {}
        for key in keys:
            results[key] = extract(data, key)

        return results

    def get_body(self):
        return self.rfile.read(int(self.headers["Content-Length"]))

    def _parse_query(self, path):
        queries = {}
        if "?" in path:
            query_string = path.split("?")[1]
            for pair in query_string.split("&"):
                key, value = pair.split("=")
                queries[key] = value
        return queries

    def _parse_input(self, body):
        form_data = {}
        if not body:
            return form_data
        content_type = self.headers.get("Content-Type", "")
        if content_type.startswith("application/x-www-form-urlencoded"):
            form_data = parse_qs(body.decode("utf-8"))
            # Parse each value as a single string instead of a list
            form_data = {k: v[0] for k, v in form_data.items()}
        elif content_type.startswith("application/json"):
            form_data = json.loads(body.decode("utf-8"))
        elif content_type.startswith("multipart/form-data"):
            # Parse the multipart form data and extract each field's value
            fields = cgi.FieldStorage(
                fp=io.BytesIO(body),
                headers=self.headers,
                environ={"REQUEST_METHOD": "POST"},
            )
            for field in fields.list:
                if field.filename:
                    form_data[field.name] = field
                else:
                    form_data[field.name] = field.value
        else:
            # Treat all other content types as plain text
            form_data = body.decode("utf-8")
        return form_data
