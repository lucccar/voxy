import re


class Words:
    @staticmethod
    def count(word: str, delimiters: list) -> int:
        if delimiters == []:
            return 1
        regex_delimiter_expression = "|".join(delimiters)
        words = re.split(regex_delimiter_expression, word)
        words = set(filter(lambda w: w != "", words))
        words = list(map(lambda w: w.strip(), words))

        return len(words)
