from pathlib import Path

import click

from mfmt.juman import Juman
from mfmt.kytea import Kytea
from mfmt.mecab import Mecab


@click.group()
def main() -> None:
    pass


@main.command()
@click.argument("input-txt", type=click.Path(path_type=Path))
def m2k(input_txt: Path) -> None:
    with open(input_txt) as file:
        lines = file.readlines()

    mecab = Mecab()
    lines = mecab.to_kytea(lines)

    for line in lines:
        print(line)


@main.command()
@click.argument("input-txt", type=click.Path(path_type=Path))
def j2m(input_txt: Path) -> None:
    with open(input_txt) as file:
        lines = file.readlines()

    juman = Juman()
    lines = juman.to_mecab(lines)

    for line in lines:
        print(line)


@main.command()
@click.argument("input-txt", type=click.Path(path_type=Path))
def k2m(input_txt: Path) -> None:
    with open(input_txt) as file:
        lines = file.readlines()

    kytea = Kytea()
    lines = kytea.to_mecab(lines)

    for line in lines:
        print(line)


if __name__ == "__main__":
    main()
