from mfmt.mecab import Mecab


def test_to_juman() -> None:
    with open("tests/mecab/input.txt") as file:
        input_lines = file.read().splitlines()

    mecab = Mecab()
    actual_lines = mecab.to_juman(input_lines)

    with open("tests/mecab/output_juman.txt") as file:
        expected_lines = file.read().splitlines()

    assert actual_lines == expected_lines


def test__to_kytea() -> None:
    mecab = Mecab()
    lines = [
        "今日	名詞,副詞可能,*,*,*,*,今日,キョウ,キョー",
        "は	助詞,係助詞,*,*,*,*,は,ハ,ワ",
        "雨	名詞,一般,*,*,*,*,雨,アメ,アメ",
        "です	助動詞,*,*,*,特殊・デス,基本形,です,デス,デス",
        "。	記号,句点,*,*,*,*,。,。,。",
    ]
    actual = mecab._to_kytea(lines)
    expected = "今日/名詞/きょう は/助詞/は 雨/名詞/あめ です/助動詞/です 。/記号/。"
    assert actual == expected


def test__split() -> None:
    line = "今日	名詞,副詞可能,*,*,*,*,今日,キョウ,キョー"
    mecab = Mecab()
    actual = mecab._split(line)
    expected = ("今日", "名詞", "副詞可能", "きょう")
    assert actual == expected
