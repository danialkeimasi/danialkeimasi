import os
import typer


def main(arg: str):
    typer.echo(f"echo {arg}")


if __name__ == "__main__":
    typer.run(main)
