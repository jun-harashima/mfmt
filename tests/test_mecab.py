import pytest

from mfmt.mecab import Mecab


@pytest.fixture
def mecab() -> Mecab:
    mecab = Mecab()
    return mecab


@pytest.fixture
def lines() -> list[str]:
    lines = [
        "今日	名詞,副詞可能,*,*,*,*,今日,キョウ,キョー",
        "は	助詞,係助詞,*,*,*,*,は,ハ,ワ",
        "雨	名詞,一般,*,*,*,*,雨,アメ,アメ",
        "です	助動詞,*,*,*,特殊・デス,基本形,です,デス,デス",
        "。	記号,句点,*,*,*,*,。,。,。",
    ]
    return lines


def test__to_juman(mecab, lines) -> None:
    actual = mecab._to_juman(lines)
    expected = [
        "今日 きょう * 名詞 * 副詞可能 * * * * * *",
        "は は * 助詞 * 係助詞 * * * * * *",
        "雨 あめ * 名詞 * 一般 * * * * * *",
        "です です * 助動詞 * * * * * * * *",
        "。 。 * 記号 * 句点 * * * * * *",
    ]
    assert actual == expected


def test__to_kytea(mecab, lines) -> None:
    actual = mecab._to_kytea(lines)
    expected = ["今日/名詞/きょう は/助詞/は 雨/名詞/あめ です/助動詞/です 。/記号/。"]
    assert actual == expected


def test__split(mecab, lines) -> None:
    actual = mecab._split(lines[0])
    expected = ("今日", "名詞", "副詞可能", "きょう")
    assert actual == expected
