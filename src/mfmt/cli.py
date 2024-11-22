from pathlib import Path

import click
from mfmt.kytea import Kytea


@click.group()
def main():
    pass


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
