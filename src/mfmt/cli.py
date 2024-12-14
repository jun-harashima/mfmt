from pathlib import Path

import click

from mfmt.juman import Juman
from mfmt.kytea import Kytea
from mfmt.mecab import Mecab
from mfmt.vaporetto import Vaporetto


@click.group()
def main() -> None:
    pass


@main.command()
@click.argument("input-txt", type=click.Path(path_type=Path))
def m2j(input_txt: Path) -> None:
    mecab = Mecab()
    mecab.to_juman(input_txt)


@main.command()
@click.argument("input-txt", type=click.Path(path_type=Path))
def m2k(input_txt: Path) -> None:
    mecab = Mecab()
    mecab.to_kytea(input_txt)


@main.command()
@click.argument("input-txt", type=click.Path(path_type=Path))
def j2m(input_txt: Path) -> None:
    juman = Juman()
    juman.to_mecab(input_txt)

@main.command()
@click.argument("input-txt", type=click.Path(path_type=Path))
def j2k(input_txt: Path) -> None:
    juman = Juman()
    juman.to_kytea(input_txt)


@main.command()
@click.argument("input-txt", type=click.Path(path_type=Path))
def k2m(input_txt: Path) -> None:
    kytea = Kytea()
    kytea.to_mecab(input_txt)


@main.command()
@click.argument("input-txt", type=click.Path(path_type=Path))
def k2j(input_txt: Path) -> None:
    kytea = Kytea()
    kytea.to_juman(input_txt)


@main.command()
@click.argument("input-txt", type=click.Path(path_type=Path))
def v2m(input_txt: Path) -> None:
    vaporetto = Vaporetto()
    vaporetto.to_mecab(input_txt)


@main.command()
@click.argument("input-txt", type=click.Path(path_type=Path))
def v2j(input_txt: Path) -> None:
    vaporetto = Vaporetto()
    vaporetto.to_juman(input_txt)


if __name__ == "__main__":
    main()
