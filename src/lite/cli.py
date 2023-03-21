import click

from .core.lite import Lite

@click.group()
def lite():
    pass

@lite.command()
@click.option("--port", type=int, default=8080, help="The port number to bind the server to (default: 8080)")
def serve(port):
    from .app import app
    app.port = port
    app.start()

@lite.command()
def test():
    click.echo("Running tests...")

@lite.command()
def migrate():
    click.echo("Running migrations...")

if __name__ == "__main__":
    lite()