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
        "よい	形容詞,自立,*,*,形容詞・アウオ段,基本形,よい,ヨイ,ヨイ",
        "天気	名詞,一般,*,*,*,*,天気,テンキ,テンキ",
        "です	助動詞,*,*,*,特殊・デス,基本形,です,デス,デス",
        "。	記号,句点,*,*,*,*,。,。,。",
    ]
    return lines


def test__to_juman(mecab: Mecab, lines: list[str]) -> None:
    actual = mecab._to_juman(lines)
    expected = [
        "今日 きょう * 名詞 * 副詞可能 * * * * * *",
        "は は * 助詞 * 係助詞 * * * * * *",
        "よい よい * 形容詞 * 自立 * * * * * *",
        "天気 てんき * 名詞 * 一般 * * * * * *",
        "です です * 助動詞 * * * * * * * *",
        "。 。 * 記号 * 句点 * * * * * *",
    ]
    assert actual == expected


def test__to_kytea(mecab: Mecab, lines: list[str]) -> None:
    actual = mecab._to_kytea(lines)
    expected = [
        "今日/名詞/きょう は/助詞/は よい/形容詞/よい 天気/名詞/てんき です/助動詞/です 。/記号/。",  # noqa: E501
    ]
    assert actual == expected


def test__to_vaporetto(mecab: Mecab, lines: list[str]) -> None:
    actual = mecab._to_vaporetto(lines)
    expected = [
        "今日/名詞-副詞可能/きょう は/助詞-係助詞/は よい/形容詞-自立/よい 天気/名詞-一般/てんき です/助動詞/です 。/記号-句点/。",  # noqa: E501
    ]
    assert actual == expected


def test__split(mecab: Mecab, lines: list[str]) -> None:
    actual = mecab._split(lines[0])
    expected = ("今日", "名詞", "副詞可能", "きょう")
    assert actual == expected
