"""Console script for fang333."""
import fang333

import typer
from rich.console import Console

app = typer.Typer()
console = Console()


@app.command()
def main():
    """Console script for fang333."""
    console.print("Replace this message by putting your code into "
               "fang333.cli.main")
    console.print("See Typer documentation at https://typer.tiangolo.com/")
    


if __name__ == "__main__":
    app()
