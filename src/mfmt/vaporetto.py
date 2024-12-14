import sys
from pathlib import Path
from typing import Callable


class Vaporetto():
    def __init__(self) -> None:
        pass

    def to_mecab(self, input_txt: Path) -> None:
        pass
    #     self._convert(input_txt, self._to_mecab)

    # def to_juman(self, input_txt: Path) -> None:
    #     pass

    # def to_kytea(self, input_txt: Path) -> None:
    #     pass

    def _convert(
        self,
        input_txt: Path,
        _to_analyzer: Callable[[str], list[str]],
    ) -> None:
        with open(input_txt) as file:
            for line in file:
                line = line.rstrip("\n")
                output_lines = _to_analyzer(line)
                for output_line in output_lines:
                    print(output_line)
                print("EOS")

    def _to_mecab(self, line: str) -> list[str]:
        output_lines = []
        words = self._split(line)
        for word in words:
            # When processing English sentences, it may fail to predict the part of
            # speech for some words. See test_vaporetto.py for details.
            if "/" not in word:
                continue

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

            categories = hinshi.split("-")

            # e.g. [名詞, 普通名詞, 副詞可能]
            # e.g. [補助記号, 句点]
            if len(categories) > 1:
                hinshi1, hinshi2 = categories[0], categories[-1]
            # e.g. 助動詞
            elif len(categories) == 1:
                hinshi1, hinshi2 = categories[0], "*"
            else:
                sys.stderr.write(f"Unexpected categories: {categories}\n")
                sys.exit(1)

            output_line = f"{midashi}\t{hinshi1},{hinshi2},*,*,*,*,*,{yomi},*"
            output_lines.append(output_line)
        return output_lines

    def _split(self, line: str) -> list[str]:
        words = line.split(" ")
        return words
