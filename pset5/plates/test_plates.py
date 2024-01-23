from plates import is_valid

def test_lenght():
    assert is_valid("a") == False
    assert is_valid("AsDfGhJ") == False
    assert is_valid("AsDfGh") == True
    
def test_start_with_two_letters():
    assert is_valid("AA") == True
    assert is_valid("A2") == False
    assert is_valid("2A") == False
    assert is_valid("22") == False
    
def test_number_place():
    assert is_valid("231dfg") == False
    assert is_valid("as567u") == False
    assert is_valid("asd89") == True
    
def test_zero():
    assert is_valid("ABC068") == False
    assert is_valid("ABC680") == True
    
def test_punctuation():
    assert is_valid("!ERT54") == False
    assert is_valid("ZXC,89") == False
    
