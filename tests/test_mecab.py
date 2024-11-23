from mfmt.mecab import Mecab


def test_to_kytea() -> None:
    with open("tests/mecab/input.txt") as file:
        input_lines = file.read().splitlines()

    mecab = Mecab()
    actual_lines = mecab.to_kytea(input_lines)

    with open("tests/mecab/output_kytea.txt") as file:
        expected_lines = file.read().splitlines()

    assert actual_lines == expected_lines
