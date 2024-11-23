from jaconv import hira2kata


class Kytea:
    def __init__(self) -> None:
        pass

    def to_mecab(self, input_lines: list[str]) -> list[str]:
        output_lines = []
        for line in input_lines:
            for word in line.split():
                midashi, hinshi, yomi = word.split("/")
                yomi = hira2kata(yomi)
                line = f"{midashi}\t{hinshi},*,*,*,*,*,*,{yomi},*"
                output_lines.append(line)
            output_lines.append("EOS")
        return output_lines
