from typing import List


class Mecab:
    def __init__(self) -> None:
        pass

    def to_kytea(self, input_lines: List[str]) -> List[str]:
        output_lines = []
        output_words = []
        for input_line in input_lines:
            input_line = input_line.rstrip("\n")

            if input_line == "EOS":
                output_line = " ".join(output_words) + "\n"
                output_lines.append(output_line)
                output_words = []
                continue

            midashi, rest = input_line.split("\t")
            features = rest.split(",")
            hinshi = features[0]
            yomi = features[1]
            output_word = f"{midashi}/{hinshi}/{yomi}"
            output_words.append(output_word)
        return output_lines
