from jaconv import kata2hira


class Mecab:
    def __init__(self) -> None:
        pass

    def to_juman(self, input_lines: list[str]) -> list[str]:
        output_lines = []
        for input_line in input_lines:
            if input_line == "EOS":
                output_lines.append("EOS")
            else:
                midashi, hinshi1, hinshi2, yomi = self._split(input_line)
                output_line = f"{midashi} {yomi} * {hinshi1} * {hinshi2} * * * * * *"
                output_lines.append(output_line)
        return output_lines

    def to_kytea(self, input_lines: list[str]) -> list[str]:
        output_lines = []
        output_words: list[str] = []
        for input_line in input_lines:
            if input_line == "EOS":
                output_line = " ".join(output_words)
                output_lines.append(output_line)
                output_words = []
            else:
                midashi, hinshi1, hinshi2, yomi = self._split(input_line)
                output_word = f"{midashi}/{hinshi1}/{yomi}"
                output_words.append(output_word)
        return output_lines

    def _split(self, line: str) -> tuple[str, str, str, str]:
        midashi, rest = line.split("\t")
        features = rest.split(",")
        hinshi1 = features[0]
        hinshi2 = features[1]
        yomi: str = kata2hira(features[7])
        return midashi, hinshi1, hinshi2, yomi
