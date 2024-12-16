from pathlib import Path
from typing import Callable

from jaconv import kata2hira


class Mecab:
    def __init__(self) -> None:
        pass

    def to_juman(self, input_txt: Path) -> None:
        self._convert(input_txt, self._to_juman)

    def to_kytea(self, input_txt: Path) -> None:
        self._convert(input_txt, self._to_kytea, print_eos=False)

    def to_vaporetto(self, input_txt: Path) -> None:
        self._convert(input_txt, self._to_vaporetto, print_eos=False)

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
                    if print_eos:
                        print("EOS")
                    lines = []
                else:
                    lines.append(line)

    def _to_juman(self, lines: list[str]) -> list[str]:
        output_lines = []
        for line in lines:
            midashi, hinshi1, hinshi2, yomi = self._split(line)
            output_line = f"{midashi} {yomi} * {hinshi1} * {hinshi2} * * * * * *"
            output_lines.append(output_line)
        return output_lines

    def _to_kytea(self, lines: list[str]) -> list[str]:
        words = []
        for line in lines:
            midashi, hinshi1, _, yomi = self._split(line)
            word = f"{midashi}/{hinshi1}/{yomi}"
            words.append(word)
        output_line = " ".join(words)
        return [output_line]

    def _to_vaporetto(self, lines: list[str]) -> list[str]:
        words = []
        for line in lines:
            midashi, hinshi1, hinshi2, yomi = self._split(line)
            if hinshi2 == "*":
                word = f"{midashi}/{hinshi1}/{yomi}"
            else:
                word = f"{midashi}/{hinshi1}-{hinshi2}/{yomi}"
            words.append(word)
        output_line = " ".join(words)
        return [output_line]

    def _split(self, line: str) -> tuple[str, str, str, str]:
        midashi, rest = line.split("\t")
        features = rest.split(",")
        hinshi1 = features[0]
        hinshi2 = features[1]
        yomi: str = kata2hira(features[7])
        return midashi, hinshi1, hinshi2, yomi
