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
        'よい よい よい 形容詞 3 * 0 イ形容詞アウオ段 18 基本形 2 "代表表記:良い/よい 反義:形容詞:悪い/わるい"',  # noqa: E501
        '天気 てんき 天気 名詞 6 普通名詞 1 * 0 * 0 "代表表記:天気/てんき カテゴリ:抽象物"',  # noqa: E501
        'です です だ 判定詞 4 * 0 判定詞 25 デス列基本形 27 NIL',
        '。 。 。 特殊 1 句点 1 * 0 * 0 NIL',
    ]
    return lines

def test__to_mecab(juman: Juman, lines: list[str]) -> None:
    actual = juman._to_mecab(lines)
    expected = [
        "今日	名詞,時相名詞,*,*,*,*,今日,キョウ,*",
        "は	助詞,副助詞,*,*,*,*,は,ハ,*",
        "よい	形容詞,*,*,*,*,*,よい,ヨイ,*",
        "天気	名詞,普通名詞,*,*,*,*,天気,テンキ,*",
        "です	判定詞,*,*,*,*,*,だ,デス,*",
        "。	特殊,句点,*,*,*,*,。,。,*",
    ]
    assert actual == expected


def test__to_kytea(juman: Juman, lines: list[str]) -> None:
    actual = juman._to_kytea(lines)
    expected = [
        "今日/名詞/きょう は/助詞/は よい/形容詞/よい 天気/名詞/てんき です/判定詞/です 。/特殊/。",  # noqa: E501
    ]
    assert actual == expected


def test__split() -> None:
    line = '今日 きょう 今日 名詞 6 時相名詞 10 * 0 * 0 "代表表記:今日/きょう カテゴリ:時間"'  # noqa: E501
    juman = Juman()
    actual = juman._split(line)
    expected = ("今日", "名詞", "時相名詞", "きょう", "今日")
    assert actual == expected
