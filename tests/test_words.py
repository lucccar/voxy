from ..app.services.words import Words

test_map = {3: {"word": "hello, world, world!", "delimeter": ","}}
test_map_unique = {2: {"word": "hello, world, world!", "delimeter": ","}}


def test_words():
    for k, v in test_map.items():
        count = Words.count(test_map[k]["word"], test_map[k]["delimeter"])
        assert k == count


def test_words_unique():
    for k, v in test_map.items():
        count = Words.count(v["word"], v["delimeter"])
        assert k == count
