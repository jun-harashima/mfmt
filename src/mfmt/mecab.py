class Mecab:
    def __init__(self) -> None:
        pass

    def to_kytea(self, input_lines: list[str]) -> list[str]:
        output_lines = []
        output_words: list[str] = []
        for input_line in input_lines:
            if input_line == "EOS":
                output_line = " ".join(output_words)
                output_lines.append(output_line)
                output_words = []
            else:
                midashi, rest = input_line.split("\t")
                hinshi, yomi = rest.split(",")[:2]
                output_word = f"{midashi}/{hinshi}/{yomi}"
                output_words.append(output_word)
        return output_lines
