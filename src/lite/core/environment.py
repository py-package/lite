from dotenv import load_dotenv
import os


class Environment:
    def __init__(self):
        load_dotenv()
        self.env = os.environ

    def __call__(self, key=None, default=None):
        if key is None:
            return self.env
        return self.env.get(key, default)
    
env = Environment()
