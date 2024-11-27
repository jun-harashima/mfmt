import re
from pathlib import Path
from typing import Callable

from jaconv import hira2kata


class Kytea:
    def __init__(self) -> None:
        self.split_pattern = re.compile(r"(?:[^\s]+?/[^\s]+?/[^\s]+)")

    def to_mecab(self, input_txt: Path) -> None:
        self._convert(input_txt, self._to_mecab)

    def to_juman(self, input_txt: Path) -> None:
        self._convert(input_txt, self._to_juman)

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
            midashi, hinshi, yomi = word.split("/")
            yomi = hira2kata(yomi)
            output_line = f"{midashi}\t{hinshi},*,*,*,*,*,*,{yomi},*"
            output_lines.append(output_line)
        return output_lines

    def _to_juman(self, line: str) -> list[str]:
        output_lines = []
        words = self._split(line)
        for word in words:
            midashi, hinshi, yomi = word.split("/")
            output_line = f"{midashi} {yomi} * {hinshi} * * * * * * * *"
            output_lines.append(output_line)
        return output_lines

    def _split(self, line: str) -> list[str]:
        line = line.replace(r"\ ", "<space>")
        words = self.split_pattern.findall(line)
        words = [word.replace("<space>", r"\ ") for word in words]
        return words
