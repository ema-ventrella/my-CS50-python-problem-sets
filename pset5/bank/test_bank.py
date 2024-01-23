from bank import value

def test_default():
    assert value("hello") == 0
    assert value("Hello") == 0
    assert value("HELLO") == 0
    
def test_h():
    assert value("hey") == 20
    assert value("hi") == 20
    assert value("how are you?") == 20
    
def test_no_h_words():
    assert value("What's up?") == 100
    assert value("Welcome!?") == 100
    assert value("Boring.") == 100
    
def test_UPPERCASE():
    assert value("WHAT'S UP??") == 100
    assert value("WELCOME!") == 100
    assert value("BORING.") == 100
    