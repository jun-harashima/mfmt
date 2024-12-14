import sys
from pathlib import Path
from typing import Callable

from jaconv import kata2hira


class Vaporetto():
    def __init__(self) -> None:
        pass

    def to_mecab(self, input_txt: Path) -> None:
        self._convert(input_txt, self._to_mecab)

    def to_juman(self, input_txt: Path) -> None:
        self._convert(input_txt, self._to_juman)

    def to_kytea(self, input_txt: Path) -> None:
        self._convert(input_txt, self._to_kytea, print_eos=False)

    def _convert(
        self,
        input_txt: Path,
        _to_analyzer: Callable[[str], list[str]],
        print_eos: bool = True,
    ) -> None:
        with open(input_txt) as file:
            for line in file:
                line = line.rstrip("\n")
                output_lines = _to_analyzer(line)
                for output_line in output_lines:
                    print(output_line)
                if print_eos:
                    print("EOS")

    def _to_mecab(self, line: str) -> list[str]:
        output_lines = []
        words = self._split(line)
        for word in words:
            # When processing English sentences, it may fail to predict the part of
            # speech for some words. See test_vaporetto.py for details.
            if "/" not in word:
                continue

            midashi, hinshi1, hinshi2, hinshi3, yomi = self._extract(word)

            # e.g. [補助記号, 句点, *]
            # e.g. [助動詞, *, *]
            if hinshi3 == "*":
                output_line = f"{midashi}\t{hinshi1},{hinshi2},*,*,*,*,*,{yomi},*"
            # e.g. [名詞, 普通名詞, 副詞可能]
            else:
                output_line = f"{midashi}\t{hinshi1},{hinshi3},*,*,*,*,*,{yomi},*"

            output_lines.append(output_line)
        return output_lines

    def _to_juman(self, line: str) -> list[str]:
        output_lines = []
        words = self._split(line)
        for word in words:
            # When processing English sentences, it may fail to predict the part of
            # speech for some words. See test_vaporetto.py for details.
            if "/" not in word:
                continue
            midashi, hinshi1, hinshi2, _, yomi = self._extract(word)
            output_line = f"{midashi} {kata2hira(yomi)} * {hinshi1} * {hinshi2} * * * * * *"  # noqa: E501
            output_lines.append(output_line)
        return output_lines

    def _to_kytea(self, line: str) -> list[str]:
        output_words = []
        words = self._split(line)
        for word in words:
            # When processing English sentences, it may fail to predict the part of
            # speech for some words. See test_vaporetto.py for details.
            if "/" not in word:
                continue
            midashi, hinshi1, hinshi2, hinshi3, yomi = self._extract(word)
            hinshi = "-".join([h for h in [hinshi1, hinshi2, hinshi3] if h != "*"])
            yomi = kata2hira(yomi)
            if yomi == "*":
                output_word = f"{midashi}/{hinshi}"
            else:
                output_word = f"{midashi}/{hinshi}/{yomi}"
            output_words.append(output_word)
        output_line = " ".join(output_words)
        return [output_line]

    def _extract(self, word: str) -> tuple[str, str, str, str, str]:
        features = word.split("/")

        # e.g. 今日/名詞-普通名詞-副詞可能/キョウ
        # e.g. です/助動詞/デス
        if len(features) == 3:
            midashi, hinshi, yomi = features
        # e.g. 。/補助記号-句点
        elif len(features) == 2:
            midashi, hinshi, yomi = features + ["*"]
        else:
            sys.stderr.write(f"Unexpected features: {features}\n")
            sys.exit(1)

        # e.g. [名詞, 普通名詞, 副詞可能]
        # e.g. [補助記号, 句点, *]
        # e.g. [助動詞, *, *]
        hinshi1, hinshi2, hinshi3 = (hinshi.split("-") + ["*"] * 3)[:3]

        return midashi, hinshi1, hinshi2, hinshi3, yomi

    def _split(self, line: str) -> list[str]:
        words = line.split(" ")
        return words
