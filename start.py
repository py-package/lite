from src.lite.app import app

def application(environ, start_response):
    print(environ)
    app.start()

if __name__ == '__main__':
    app.start()