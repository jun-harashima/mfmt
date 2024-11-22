from typing import List


class Kytea():
    def __init__(self) -> None:
        pass

    def to_mecab(self, input_lines: List[str]) -> List[str]:
        output_lines = []
        for input_line in input_lines:
            for word in input_line.split():
                midashi, hinshi, yomi = word.split("/")
                output_line = f"{midashi}\t{hinshi},{yomi}\n"
                output_lines.append(output_line)
            output_lines.append("EOS\n")
        return output_lines
