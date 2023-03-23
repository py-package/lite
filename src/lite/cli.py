import sys

import click
import hupper


@click.group()
def lite():
    pass


@lite.command()
@click.option(
    "--port",
    type=int,
    default=8000,
    help="The port number to bind the server to (default: 8000)",
)
def serve(port):
    from .app import application

    application.port = port

    reloader = hupper.start_reloader("lite.cli.start")
    reloader.watch_files(["lite"])
    reloader.watch_files(["lite.py"])
    reloader.watch_files(["lite/__init__.py"])
    reloader.watch_files(["lite/app.py"])

    application.start()


@lite.command()
def test():
    click.echo("Running tests...")


@lite.command()
def migrate():
    click.echo("Running migrations...")


def start(args=sys.argv[1:]):
    lite()


if __name__ == "__main__":
    start()
