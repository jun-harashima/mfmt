from mfmt.juman import Juman


def test_to_mecab() -> None:
    with open("tests/juman/input.txt") as file:
        input_lines = file.read().splitlines()

    juman = Juman()
    actual_lines = juman.to_mecab(input_lines)

    with open("tests/juman/output_mecab.txt") as file:
        expected_lines = file.read().splitlines()

    assert actual_lines == expected_lines
