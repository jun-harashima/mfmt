import pytest

from mfmt.kytea import Kytea


@pytest.fixture
def kytea() -> Kytea:
    kytea = Kytea()
    return kytea


@pytest.fixture
def line() -> str:
    line = "今日/名詞/きょう は/助詞/は よ/形容詞/よ い/語尾/い 天気/名詞/てんき で/助動詞/で す/語尾/す 。/補助記号/。"  # noqa: E501
    return line


def test__to_mecab(kytea: Kytea, line: str) -> None:
    actual = kytea._to_mecab(line)
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
