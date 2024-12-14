from pathlib import Path


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

    # def _convert(
    #     self,
    #     input_txt: Path,
    #     _to_analyzer: Callable[[str], list[str]],
    # ) -> None:
    #     with open(input_txt) as file:
    #         for line in file:
    #             line = line.rstrip("\n")
    #             output_lines = _to_analyzer(line)
    #             for output_line in output_lines:
    #                 print(output_line)
    #             print("EOS")

    # def _to_mecab(self, line: str) -> list[str]:
    #     output_lines = []
    #     words = self._split(line)
    #     for word in words:
    #         midashi, hinshi, yomi = word.split("/")
    #         yomi = hira2kata(yomi)
    #         output_line = f"{midashi}\t{hinshi},*,*,*,*,*,*,{yomi},*"
    #         output_lines.append(output_line)
    #     return output_lines

    def _split(self, line: str) -> list[str]:
        words = line.split(" ")
        return words
