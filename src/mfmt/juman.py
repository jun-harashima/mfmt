from jaconv import hira2kata


class Juman:
    def __init__(self) -> None:
        pass

    def to_mecab(self, input_lines: list[str]) -> list[str]:
        output_lines = []
        for line in input_lines:
            if line == "EOS":
                output_lines.append("EOS")
            elif line.startswith("@"):
                pass
            else:
                midashi, hinshi1, hinshi2, yomi, genkei = self._split(line)
                yomi = hira2kata(yomi)
                line = f"{midashi}\t{hinshi1},{hinshi2},*,*,*,*,{genkei},{yomi},*"
                output_lines.append(line)
        return output_lines


    def to_kytea(self, input_lines: list[str]) -> list[str]:
        output_lines = []
        output_words: list[str] = []
        for line in input_lines:
            if line == "EOS":
                output_line = " ".join(output_words)
                output_lines.append(output_line)
                output_words = []
            elif line.startswith("@"):
                pass
            else:
                midashi, hinshi1, _, yomi,_ = self._split(line)
                output_word = f"{midashi}/{hinshi1}/{yomi}"
                output_words.append(output_word)
        return output_lines


    def _split(self, line: str) -> tuple[str, str, str, str, str]:
        features = line.split()
        midashi, yomi, genkei, hinshi1, _, hinshi2 = features[:6]
        return midashi, hinshi1, hinshi2, yomi, genkei
