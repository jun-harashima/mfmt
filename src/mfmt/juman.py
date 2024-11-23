from pathlib import Path

from jaconv import hira2kata


class Juman:
    def __init__(self) -> None:
        pass

    def to_mecab(self, input_txt: Path) -> None:
        with open(input_txt) as file:
            lines: list[str] = []
            for line in file:
                line = line.rstrip("\n")
                if line == "EOS":
                    output_lines = self._to_mecab(lines)
                    for output_line in output_lines:
                        print(output_line)
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

    def to_kytea(self, input_txt: Path) -> None:
        with open(input_txt) as file:
            lines: list[str] = []
            for line in file:
                line = line.rstrip("\n")
                if line == "EOS":
                    output_line = self._to_kytea(lines)
                    print(output_line)
                    lines = []
                elif line.startswith("@"):
                    pass
                else:
                    lines.append(line)

    def _to_kytea(self, lines: list[str]) -> str:
        words = []
        for line in lines:
            midashi, hinshi1, _, yomi,_ = self._split(line)
            word = f"{midashi}/{hinshi1}/{yomi}"
            words.append(word)
        output_line = " ".join(words)
        return output_line


    def _split(self, line: str) -> tuple[str, str, str, str, str]:
        features = line.split()
        midashi, yomi, genkei, hinshi1, _, hinshi2 = features[:6]
        return midashi, hinshi1, hinshi2, yomi, genkei
