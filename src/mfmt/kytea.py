from pathlib import Path

from jaconv import hira2kata


class Kytea:
    def __init__(self) -> None:
        pass

    def to_mecab(self, input_txt: Path) -> None:
        with open(input_txt) as file:
            for line in file:
                output_lines = self._to_mecab(line)
                for output_line in output_lines:
                    print(output_line)
                print("EOS")

    def _to_mecab(self, line: str) -> list[str]:
        output_lines = []
        for word in line.split():
            midashi, hinshi, yomi = word.split("/")
            yomi = hira2kata(yomi)
            output_line = f"{midashi}\t{hinshi},*,*,*,*,*,*,{yomi},*"
            output_lines.append(output_line)
        return output_lines
