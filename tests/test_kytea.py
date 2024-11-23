from mfmt.kytea import Kytea


def test_to_mecab() -> None:
    with open("tests/kytea/input.txt") as file:
        input_lines = file.read().splitlines()

    kytea = Kytea()
    actual_lines = kytea.to_mecab(input_lines)

    with open("tests/kytea/output_mecab.txt") as file:
        expected_lines = file.read().splitlines()

    assert actual_lines == expected_lines
