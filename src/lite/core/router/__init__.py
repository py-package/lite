import re


class TrieNode:
    def __init__(self):
        self.children = {}
        self.handler = None
        self.path = ""

class Router:
    def __init__(self):
        self.root = TrieNode()

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
        parts = path.strip("/").split("/")
        current_node = self.root
        for part in parts:
            if ":" in part:
                part = "<var>"
            if part not in current_node.children:
                current_node.children[part] = TrieNode()
            current_node = current_node.children[part]
        current_node.handler = handler
        current_node.path = path

    def get_handler(self, path, method):
        parts = path.strip("/").split("/")
        current_node = self.root
        path_vars = {}
        for part in parts:
            if current_node is None:
                return None, {}
            if part in current_node.children:
                current_node = current_node.children[part]
            elif "<var>" in current_node.children:
                current_node = current_node.children["<var>"]
                path_vars[current_node.path.split(":")[-1]] = part
            else:
                return None, {}
        handler = current_node.handler
        return handler, path_vars