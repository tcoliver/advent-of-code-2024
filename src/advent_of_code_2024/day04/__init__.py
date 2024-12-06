import re
from pathlib import Path

from rich import print


def part_1():
    """Day 4, Part 1: Ceres Search

    "Looks like the Chief's not here. Next!" One of The Historians pulls out a device
    and pushes the only button on it. After a brief flash, you recognize the interior
    of the Ceres monitoring station!

    As the search for the Chief continues, a small Elf who lives on the station tugs
    on your shirt; she'd like to know if you could help her with her word search (your
    puzzle input). She only has to find one word: XMAS.

    This word search allows words to be horizontal, vertical, diagonal, written
    backwards, or even overlapping other words. It's a little unusual, though, as
    you don't merely need to find one instance of XMAS - you need to find all of
    them. Here are a few ways XMAS might appear, where irrelevant characters have
    been replaced with .:

    ..X...
    .SAMX.
    .A..A.
    XMAS.S
    .X....

    The actual word search will be full of letters instead. For example:

    MMMSXXMASM
    MSAMXMSMSA
    AMXSXMAAMM
    MSAMASMSMX
    XMASAMXAMM
    XXAMMXXAMA
    SMSMSASXSS
    SAXAMASAAA
    MAMMMXMMMM
    MXMXAXMASX

    In this word search, XMAS occurs a total of 18 times; here's the same word search
    again, but where letters not involved in any XMAS have been replaced with .:

    ....XXMAS.
    .SAMXMS...
    ...S..A...
    ..A.A.MS.X
    XMASAMX.MM
    X.....XA.A
    S.S.S.S.SS
    .A.A.A.A.A
    ..M.M.M.MM
    .X.X.XMASX

    Take a look at the little Elf's word search. How many times does XMAS appear?
    """
    input = (Path(__file__).parent / "input.txt").read_text()

    rows = input.splitlines()
    row_count = len(rows)
    columns = ("".join(col) for col in zip(*rows))
    diagonal_right = (
        "".join(col) for col in zip(*(f'{"-" * i}{row}{"-" * (row_count - i)}' for i, row in enumerate(rows)))
    )
    diagonal_left = (
        "".join(col) for col in zip(*(f'{"-" * (row_count - i)}{row}{"-" * i}' for i, row in enumerate(rows)))
    )

    count = 0
    for direction in (rows, columns, diagonal_right, diagonal_left):
        for line in direction:
            count += len(re.findall(r"(?=(XMAS|SAMX))", line))

    print("Total XMAS: ", count)


def part_2():
    """Day 4, Part 2: Ceres Search

    The Elf looks quizzically at you. Did you misunderstand the assignment?

    Looking for the instructions, you flip over the word search to find that this isn't
    actually an XMAS puzzle; it's an X-MAS puzzle in which you're supposed to find two
    MAS in the shape of an X. One way to achieve that is like this:

    M.S
    .A.
    M.S

    Irrelevant characters have again been replaced with . in the above diagram. Within
    the X, each MAS can be written forwards or backwards.

    Here's the same example from before, but this time all of the X-MASes have been
    kept instead:

    .M.S......
    ..A..MSMS.
    .M.S.MAA..
    ..A.ASMSM.
    .M.S.M....
    ..........
    S.S.S.S.S.
    .A.A.A.A..
    M.M.M.M.M.
    ..........

    In this example, an X-MAS appears 9 times.

    Flip the word search from the instructions back over to the word search side and
    try again. How many times does an X-MAS appear?
    """
    input = (Path(__file__).parent / "input.txt").read_text()

    rows = input.splitlines()
    rc = len(rows)
    diagonal_right = (
        "".join(col) for col in zip(*(f'{"-" * (rc - 1 - i)}{row}{"-" * (i)}' for i, row in enumerate(rows)))
    )
    diagonal_left = (
        "".join(col) for col in zip(*(f'{"-" * (rc - 1 - i)}{row}{"-" * (i)}' for i, row in enumerate(reversed(rows))))
    )

    rset = set()
    lset = set()
    for i, (right, left) in enumerate(zip(diagonal_right, diagonal_left), start=-rc + 1):
        rrow = abs(i) + 1 if i < 0 else 1
        lrow = rc + i if i < 0 else rc
        col = 1 if i < 0 else i + 1
        offset = rrow - 1
        rset |= {
            (col + m.start(1) - offset + 1, rrow + m.start(1) - offset + 1)
            for m in re.finditer(r"(?=(MAS|SAM))", right)
        }
        lset |= {
            (col + m.start(1) - offset + 1, lrow - m.start(1) + offset - 1) for m in re.finditer(r"(?=(MAS|SAM))", left)
        }

    print("Total XMAS: ", len(rset & lset))
