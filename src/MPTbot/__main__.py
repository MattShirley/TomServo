"""Command-line interface."""
import click

from .bot import start_bot


@click.command()
@click.version_option()
def main() -> None:
    """MPTbot."""
    print("MPTbot")
    start_bot()


if __name__ == "__main__":
    main(prog_name="MPTbot")  # pragma: no cover
