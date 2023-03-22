import os
import json
import uuid

class Session:
    def __init__(self, session_id=None):
        if session_id:
            self.id = session_id
        else:
            self.id = str(uuid.uuid4())
        self.data = {}

    def get(self, key):
        return self.data.get(key)

    def set(self, key, value):
        self.data[key] = value

    def delete(self, key):
        if key in self.data:
            del self.data[key]

    def save(self):
        with open(f"session:{self.id}.json", "w") as f:
            json.dump(self.data, f)

    @classmethod
    def load(cls, session_id):
        try:
            with open(f"session:{session_id}.json", "r") as f:
                session = cls(session_id)
                session.data = json.load(f)
                return session
        except FileNotFoundError:
            return cls(session_id)