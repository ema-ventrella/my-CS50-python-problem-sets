from twttr import shorten


def test_UPPERCASE():
    assert shorten("BANANA") == "BNN"
    assert shorten("APPLE") == "PPL"
    assert shorten("MELON") == "MLN"


def test_lowercase():
    assert shorten("banana") == "bnn"
    assert shorten("apple") == "ppl"
    assert shorten("melon") == "mln"


def test_punctuation():
    assert shorten("Are you ok?") == "r y k?"
    assert shorten("I'm Joe.") == "'m J."
    assert shorten("I'm doing grate, thanks!") == "'m dng grt, thnks!"


def test_numbers():
    assert shorten("3 bananas") == "3 bnns"
    assert shorten("6 apples") == "6 ppls"
    assert shorten("2 melons") == "2 mlns"


def test_Capitalized():
    assert shorten("Banana") == "Bnn"
    assert shorten("Apple") == "ppl"
    assert shorten("Melon") == "Mln"
