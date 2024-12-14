import pytest

from mfmt.vaporetto import Vaporetto


@pytest.fixture
def vaporetto() -> Vaporetto:
    vaporetto = Vaporetto()
    return vaporetto


@pytest.fixture
def lines() -> list[str]:
    lines = [
        "今日/名詞-普通名詞-副詞可能/キョウ は/助詞-係助詞/ハ よい/形容詞-非自立可能/ヨイ 天気/名詞-普通名詞-一般/テンキ です/助動詞/デス 。/補助記号-句点",  # noqa: E501
        r"The/名詞-普通名詞-一般/ザ \ weather \  is/名詞-普通名詞-一般/イズ \ nice\  today ./補助記号-句点",  # noqa: E501
    ]
    return lines


def test__to_mecab(vaporetto: Vaporetto, lines: list[str]) -> None:
    actual = vaporetto._to_mecab(lines[0])
    expected = [
        "今日	名詞,副詞可能,*,*,*,*,*,キョウ,*",
        "は	助詞,係助詞,*,*,*,*,*,ハ,*",
        "よい	形容詞,非自立可能,*,*,*,*,*,ヨイ,*",
        "天気	名詞,一般,*,*,*,*,*,テンキ,*",
        "です	助動詞,*,*,*,*,*,*,デス,*",
        "。	補助記号,句点,*,*,*,*,*,*,*",
    ]
    assert actual == expected


def test__to_juman(vaporetto: Vaporetto, lines: list[str]) -> None:
    actual = vaporetto._to_juman(lines[0])
    expected = [
        "今日 きょう * 名詞 * 普通名詞 * * * * * *",
        "は は * 助詞 * 係助詞 * * * * * *",
        "よい よい * 形容詞 * 非自立可能 * * * * * *",
        "天気 てんき * 名詞 * 普通名詞 * * * * * *",
        "です です * 助動詞 * * * * * * * *",
        "。 * * 補助記号 * 句点 * * * * * *",
    ]
    assert actual == expected


def test_split(vaporetto: Vaporetto, lines: list[str]) -> None:
    actual = vaporetto._split(lines[0])
    expected = [
        "今日/名詞-普通名詞-副詞可能/キョウ",
        "は/助詞-係助詞/ハ",
        "よい/形容詞-非自立可能/ヨイ",
        "天気/名詞-普通名詞-一般/テンキ",
        "です/助動詞/デス",
        "。/補助記号-句点",
    ]

    # Vaporetto seems to skip outputting readings (yomi) for auxiliary symbols.
    # Additionally, when processing English sentences, it may fail to predict the part
    # of speech for some words. (You can try it here: https://vaporetto-demo.pages.dev/)
    actual = vaporetto._split(lines[1])
    expected = [
        "The/名詞-普通名詞-一般/ザ",
        "\\",
        "weather",
        "\\",
        "",
        "is/名詞-普通名詞-一般/イズ",
        "\\",
        "nice\\",
        "",
        "today",
        "./補助記号-句点",
    ]
    assert actual == expected
