import inspect
from typing import Annotated

import typer

from . import day01, day02, day03, day04, day05

app = typer.Typer(rich_markup_mode="rich")
app.command(name="d1p1")(day01.part_1)
app.command(name="d1p2")(day01.part_2)
app.command(name="d2p1")(day02.part_1)
app.command(name="d2p2")(day02.part_2)
app.command(name="d3p1")(day03.part_1)
app.command(name="d3p2")(day03.part_2)
app.command(name="d4p1")(day04.part_1)
app.command(name="d4p2")(day04.part_2)
app.command(name="d5p1")(day05.part_1)
app.command(name="d5p2")(day05.part_2)


@app.callback(no_args_is_help=True)
def main(
    ctx: typer.Context,
    source: Annotated[bool, typer.Option("--source", "-s", help="Show the source code for the problem.")] = False,
):
    """Advent of Code 2024

    The Chief Historian is always present for the big Christmas sleigh launch, but
    nobody has seen him in months! Last anyone heard, he was visiting locations that
    are historically significant to the North Pole; a group of Senior Historians has
    asked you to accompany them as they check the places they think he was most likely
    to visit.

    As each location is checked, they will mark it on their list with a star. They
    figure the Chief Historian must be in one of the first fifty places they'll look,
    so in order to save Christmas, you need to help them get fifty stars on their
    list before Santa takes off on December 25th.

    Collect stars by solving puzzles. Two puzzles will be made available on each day
    in the Advent calendar; the second puzzle is unlocked when you complete the first.
    Each puzzle grants one star. Good luck!
    """

    if source:
        cmd = typer.main.get_command(app).commands[ctx.invoked_subcommand].callback
        print(inspect.getsource(cmd))


if __name__ == "__main__":
    app()
