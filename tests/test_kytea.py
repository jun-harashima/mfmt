import pytest

from mfmt.kytea import Kytea


@pytest.fixture
def kytea() -> Kytea:
    kytea = Kytea()
    return kytea


@pytest.fixture
def lines() -> list[str]:
    lines = [
        "今日/名詞/きょう は/助詞/は よ/形容詞/よ い/語尾/い 天気/名詞/てんき で/助動詞/で す/語尾/す 。/補助記号/。",  # noqa: E501
        r"The/名詞/ＴＨＥ \ /補助記号/UNK weather/名詞/ＷＥＡＴＨＥＲ \ /補助記号/UNK is/名詞/ＩＳ \ nice\ /名詞/UNK today/名詞/ＴＯＤＡＹ ./補助記号/。",  # noqa: E501
    ]
    return lines


def test__to_mecab(kytea: Kytea, lines: list[str]) -> None:
    actual = kytea._to_mecab(lines[0])
    expected = [
        "今日	名詞,*,*,*,*,*,*,キョウ,*",
        "は	助詞,*,*,*,*,*,*,ハ,*",
        "よ	形容詞,*,*,*,*,*,*,ヨ,*",
        "い	語尾,*,*,*,*,*,*,イ,*",
        "天気	名詞,*,*,*,*,*,*,テンキ,*",
        "で	助動詞,*,*,*,*,*,*,デ,*",
        "す	語尾,*,*,*,*,*,*,ス,*",
        "。	補助記号,*,*,*,*,*,*,。,*",
    ]
    assert actual == expected


def test__to_juman(kytea: Kytea, lines: list[str]) -> None:
    actual = kytea._to_juman(lines[0])
    expected = [
        "今日 きょう * 名詞 * * * * * * * *",
        "は は * 助詞 * * * * * * * *",
        "よ よ * 形容詞 * * * * * * * *",
        "い い * 語尾 * * * * * * * *",
        "天気 てんき * 名詞 * * * * * * * *",
        "で で * 助動詞 * * * * * * * *",
        "す す * 語尾 * * * * * * * *",
        "。 。 * 補助記号 * * * * * * * *",
    ]
    assert actual == expected


def test_split(kytea: Kytea, lines: list[str]) -> None:
    actual = kytea._split(lines[0])
    expected = [
        "今日/名詞/きょう",
        "は/助詞/は",
        "よ/形容詞/よ",
        "い/語尾/い",
        "天気/名詞/てんき",
        "で/助動詞/で",
        "す/語尾/す",
        "。/補助記号/。",
    ]
    print(actual)
    assert actual == expected

    actual = kytea._split(lines[1])
    expected = [
        "The/名詞/ＴＨＥ",
        r"\ /補助記号/UNK",
        "weather/名詞/ＷＥＡＴＨＥＲ",
        r"\ /補助記号/UNK",
        "is/名詞/ＩＳ",
        r"\ nice\ /名詞/UNK",
        "today/名詞/ＴＯＤＡＹ",
        "./補助記号/。",
    ]
    assert actual == expected
