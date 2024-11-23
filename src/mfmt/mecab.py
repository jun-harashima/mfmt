from pathlib import Path

from jaconv import kata2hira


class Mecab:
    def __init__(self) -> None:
        pass

    def to_juman(self, input_txt: Path) -> None:
        with open(input_txt) as file:
            lines: list[str] = []
            for line in file:
                line = line.rstrip("\n")
                if line == "EOS":
                    output_lines = self._to_juman(lines)
                    for output_line in output_lines:
                        print(output_line)
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

    def to_kytea(self, input_txt: Path) -> None:
        with open(input_txt) as file:
            lines: list[str] = []
            for line in file:
                line = line.rstrip("\n")
                if line == "EOS":
                    output_line = self._to_kytea(lines)
                    print(output_line)
                    lines = []
                else:
                    lines.append(line)

    def _to_kytea(self, lines: list[str]) -> str:
        words = []
        for line in lines:
            midashi, hinshi1, _, yomi = self._split(line)
            word = f"{midashi}/{hinshi1}/{yomi}"
            words.append(word)
        output_line = " ".join(words)
        return output_line

    def _split(self, line: str) -> tuple[str, str, str, str]:
        midashi, rest = line.split("\t")
        features = rest.split(",")
        hinshi1 = features[0]
        hinshi2 = features[1]
        yomi: str = kata2hira(features[7])
        return midashi, hinshi1, hinshi2, yomi
