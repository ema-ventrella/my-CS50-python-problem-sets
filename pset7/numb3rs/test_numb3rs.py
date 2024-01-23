from numb3rs.numb3rs import validate

def test_one():
    assert validate("1.1.1.1") == True
    assert validate("cat") == False
    assert validate("2.4.1.3") == True

def test_two():
    assert validate("123.123.123.123") == True
    assert validate("176.189.65.12") == True
    assert validate("256.1.1.1") == False
    
def test_false():
    assert validate("342.1.1.1") == False
    assert validate("1.1.1.342") == False
    assert validate("342.342.342.342") == False