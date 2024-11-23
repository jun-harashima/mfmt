from mfmt.mecab import Mecab


def test_to_juman() -> None:
    with open("tests/mecab/input.txt") as file:
        input_lines = file.read().splitlines()

    mecab = Mecab()
    actual_lines = mecab.to_juman(input_lines)

    with open("tests/mecab/output_juman.txt") as file:
        expected_lines = file.read().splitlines()

    assert actual_lines == expected_lines


def test_to_kytea() -> None:
    with open("tests/mecab/input.txt") as file:
        input_lines = file.read().splitlines()

    mecab = Mecab()
    actual_lines = mecab.to_kytea(input_lines)

    with open("tests/mecab/output_kytea.txt") as file:
        expected_lines = file.read().splitlines()

    assert actual_lines == expected_lines


def test__split() -> None:
    line = "今日	名詞,副詞可能,*,*,*,*,今日,キョウ,キョー"
    mecab = Mecab()
    actual = mecab._split(line)
    expected = ("今日", "名詞", "副詞可能", "きょう")
    assert actual == expected
