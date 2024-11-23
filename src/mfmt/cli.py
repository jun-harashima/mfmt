from pathlib import Path
from typing import Callable

import click

from mfmt.juman import Juman
from mfmt.kytea import Kytea
from mfmt.mecab import Mecab


@click.group()
def main() -> None:
    pass


def convert(input_txt: Path, function: Callable[[list[str]], list[str]]) -> None:
    with open(input_txt) as file:
        lines = file.read().splitlines()
    lines = function(lines)
    for line in lines:
        print(line)


@main.command()
@click.argument("input-txt", type=click.Path(path_type=Path))
def m2k(input_txt: Path) -> None:
    mecab = Mecab()
    mecab.to_kytea(input_txt)


@main.command()
@click.argument("input-txt", type=click.Path(path_type=Path))
def m2j(input_txt: Path) -> None:
    mecab = Mecab()
    convert(input_txt, mecab.to_juman)


@main.command()
@click.argument("input-txt", type=click.Path(path_type=Path))
def j2m(input_txt: Path) -> None:
    juman = Juman()
    convert(input_txt, juman.to_mecab)

@main.command()
@click.argument("input-txt", type=click.Path(path_type=Path))
def j2k(input_txt: Path) -> None:
    juman = Juman()
    convert(input_txt, juman.to_kytea)


@main.command()
@click.argument("input-txt", type=click.Path(path_type=Path))
def k2m(input_txt: Path) -> None:
    kytea = Kytea()
    convert(input_txt, kytea.to_mecab)


if __name__ == "__main__":
    main()
