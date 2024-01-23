from um import count


def test_count():
    assert count("um") == 1
    assert count("um.") == 1
    assert count("um!") == 1


def test_more_count():
    assert count("um um") == 2
    assert count("um um um") == 3
    assert count("hey, um...") == 1


def test_case_insensitive():
    assert count("UM") == 1
    assert count("Um") == 1
    assert count("uM Um") == 2


def test_text():
    assert count("um, I'm not sure...") == 1
    assert count("um, um, um...") == 3
    assert count("um, Idk, um...") == 2
    
def test_um_in_words():
    assert count("instrumentation") == 0
    assert count("um.. humanitarianism, um..") == 2
