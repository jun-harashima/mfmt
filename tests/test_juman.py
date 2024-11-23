from mfmt.juman import Juman


def test_to_mecab() -> None:
    with open("tests/juman/input.txt") as file:
        input_lines = file.read().splitlines()

    juman = Juman()
    actual_lines = juman.to_mecab(input_lines)

    with open("tests/juman/output_mecab.txt") as file:
        expected_lines = file.read().splitlines()

    assert actual_lines == expected_lines


def test_to_kytea() -> None:
    with open("tests/juman/input.txt") as file:
        input_lines = file.read().splitlines()

    juman = Juman()
    actual_lines = juman.to_kytea(input_lines)

    with open("tests/juman/output_kytea.txt") as file:
        expected_lines = file.read().splitlines()

    assert actual_lines == expected_lines


def test__split() -> None:
    line = '今日 きょう 今日 名詞 6 時相名詞 10 * 0 * 0 "代表表記:今日/きょう カテゴリ:時間"'  # noqa: E501
    juman = Juman()
    actual = juman._split(line)
    expected = ("今日", "名詞", "時相名詞", "きょう", "今日")
    assert actual == expected
