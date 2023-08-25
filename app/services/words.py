import re


class Words:
    @staticmethod
    def count(word: str, delimiters: list) -> int:
        if delimiters == []:
            return 1
        regex_delimiter_expression = "|".join(delimiters)
        words = re.split(regex_delimiter_expression, word)
        words = list(filter(lambda w: w != "", words))
        # regex_delimiter_expression = "|".join(corrected_delimiters)
        # words = re.split(regex_delimiter_expression, word)
        # words = list(filter(lambda w: w != "", words))

        return len(words)
