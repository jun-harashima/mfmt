from jaconv import hira2kata


class Juman:
    def __init__(self) -> None:
        pass

    def to_mecab(self, input_lines: list[str]) -> list[str]:
        output_lines = []
        for line in input_lines:
            if line == "EOS":
                output_lines.append("EOS")
                continue
            elif line.startswith("@"):
                continue
            else:
                features = line.split()
                midashi, yomi, genkei, hinshi1, _, hinshi2 = features[:6]
                yomi = hira2kata(yomi)
                line = f"{midashi}\t{hinshi1},{hinshi2},*,*,*,*,{genkei},{yomi},*"
                output_lines.append(line)
        return output_lines
