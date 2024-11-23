import pytest

from mfmt.juman import Juman


@pytest.fixture
def juman() -> Juman:
    juman = Juman()
    return juman


@pytest.fixture
def lines() -> list[str]:
    lines = [
        '今日 きょう 今日 名詞 6 時相名詞 10 * 0 * 0 "代表表記:今日/きょう カテゴリ:時間"',  # noqa: E501
        'は は は 助詞 9 副助詞 2 * 0 * 0 NIL',
        '雨 あめ 雨 名詞 6 普通名詞 1 * 0 * 0 "代表表記:雨/あめ 漢字読み:訓 カテゴリ:抽象物"',  # noqa: E501
        'です です だ 判定詞 4 * 0 判定詞 25 デス列基本形 27 NIL',
        '。 。 。 特殊 1 句点 1 * 0 * 0 NIL',
    ]
    return lines

def test__to_mecab(juman, lines) -> None:
    actual = juman._to_mecab(lines)
    expected = [
        "今日	名詞,時相名詞,*,*,*,*,今日,キョウ,*",
        "は	助詞,副助詞,*,*,*,*,は,ハ,*",
        "雨	名詞,普通名詞,*,*,*,*,雨,アメ,*",
        "です	判定詞,*,*,*,*,*,だ,デス,*",
        "。	特殊,句点,*,*,*,*,。,。,*",
    ]
    assert actual == expected


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
