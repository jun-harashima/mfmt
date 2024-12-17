from pathlib import Path
from typing import Callable

from jaconv import hira2kata


class Juman:
    def __init__(self) -> None:
        pass

    def to_mecab(self, input_txt: Path) -> None:
        self._convert(input_txt, self._to_mecab)

    def to_kytea(self, input_txt: Path) -> None:
        self._convert(input_txt, self._to_kytea)

    def to_vaporetto(self, input_txt: Path) -> None:
        self._convert(input_txt, self._to_vaporetto)

    def _convert(
        self,
        input_txt: Path,
        _to_analyzer: Callable[[list[str]], list[str]],
        print_eos: bool = True,
    ) -> None:
        with open(input_txt) as file:
            lines: list[str] = []
            for line in file:
                line = line.rstrip("\n")
                if line == "EOS":
                    output_lines = _to_analyzer(lines)
                    for output_line in output_lines:
                        print(output_line)
                    lines = []
                if print_eos:
                    print("EOS")
                elif line.startswith("@"):
                    pass
                else:
                    lines.append(line)

    def _to_mecab(self, lines: list[str]) -> list[str]:
        output_lines = []
        for line in lines:
            midashi, hinshi1, hinshi2, yomi, genkei = self._split(line)
            yomi = hira2kata(yomi)
            line = f"{midashi}\t{hinshi1},{hinshi2},*,*,*,*,{genkei},{yomi},*"
            output_lines.append(line)
        return output_lines

    def _to_kytea(self, lines: list[str]) -> list[str]:
        words = []
        for line in lines:
            midashi, hinshi1, _, yomi, _ = self._split(line)
            word = f"{midashi}/{hinshi1}/{yomi}"
            words.append(word)
        output_line = " ".join(words)
        return [output_line]

    def _to_vaporetto(self, lines: list[str]) -> list[str]:
        words = []
        for line in lines:
            midashi, hinshi1, hinshi2, yomi, _ = self._split(line)
            if hinshi2 == "*":
                word = f"{midashi}/{hinshi1}/{yomi}"
            else:
                word = f"{midashi}/{hinshi1}-{hinshi2}/{yomi}"
            words.append(word)
        output_line = " ".join(words)
        return [output_line]

    def _split(self, line: str) -> tuple[str, str, str, str, str]:
        features = line.split()
        midashi, yomi, genkei, hinshi1, _, hinshi2 = features[:6]
        return midashi, hinshi1, hinshi2, yomi, genkei
