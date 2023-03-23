import re


class TrieNode:
    def __init__(self):
        self.children = {}
        self.handlers = {}


class Router:
    def __init__(self):
        self.root = TrieNode()
        self.special = TrieNode()
        self.special.children[":"] = TrieNode()
        self.special.children["?"] = TrieNode()

    def get(self, path, handler):
        self.add_route(path, handler, method="GET")

    def post(self, path, handler):
        self.add_route(path, handler, method="POST")

    def put(self, path, handler):
        self.add_route(path, handler, method="PUT")

    def patch(self, path, handler):
        self.add_route(path, handler, method="PATCH")

    def delete(self, path, handler):
        self.add_route(path, handler, method="DELETE")

    def options(self, path, handler):
        self.add_route(path, handler, method="OPTIONS")

    def add_route(self, path, handler, method):
        parts, queries = self._split_path(path)
        current_node = self.root

        for part in parts:
            if part.startswith(":"):
                variable_name = part[1:]
                current_node = self.special.children[":"]
                if variable_name not in current_node.handlers:
                    current_node.handlers[variable_name] = TrieNode()
                current_node = current_node.handlers[variable_name]

            elif "?" in part:
                current_node = self.special.children["?"]
                query_params = part.split("?")[1]
                for query_param in query_params.split("&"):
                    if query_param not in current_node.handlers:
                        current_node.handlers[query_param] = TrieNode()
                    current_node = current_node.handlers[query_param]

            else:
                if part not in current_node.children:
                    current_node.children[part] = TrieNode()
                current_node = current_node.children[part]

        current_node.handlers[method.upper()] = handler

    def get_handler(self, path, method):
        parts, queries = self._split_path(path)
        current_node = self.root
        path_variables = {}
        query_params = {}

        for part in parts:
            if part in current_node.children:
                current_node = current_node.children[part]

            elif ":" in self.special.children and part != "":
                current_node = self.special.children[":"]
                variable_name = list(current_node.handlers.keys())[0]
                path_variables[variable_name] = part
                current_node = current_node.handlers[variable_name]

            elif "?" in self.special.children:
                current_node = self.special.children["?"]
                query_param = part.split("?")[1]
                if query_param in current_node.handlers:
                    current_node = current_node.handlers[query_param]
                    for pair in query_param.split("&"):
                        key, value = pair.split("=")
                        query_params[key] = value
            else:
                return None

        for key, value in queries.items():
            query_params = {key: value}

        handler = current_node.handlers.get(method.upper(), None)
        if handler:
            return (handler, path_variables, query_params)
        else:
            return None

    def _split_path(self, path):
        parts = path.split("?")
        path_parts = re.split("[/]", parts[0])
        if path_parts[-1] == "":
            path_parts = path_parts[:-1]
        if len(parts) == 2:
            query_parts = parts[1].split("&")
            query_params = {}
            for query_part in query_parts:
                key, value = query_part.split("=")
                query_params[key] = value
        else:
            query_params = {}
        return path_parts, query_params

    def _check_query_params(self, path, query_params):
        query_string = path.split("?")[1]
        for param in query_params.split("&"):
            if param.split("=")[0] not in query_string:
                return False
        return True
