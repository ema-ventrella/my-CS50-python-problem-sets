from fuel import convert, gauge
import pytest

def test_convert():
    assert convert("5/10") == 50
    assert convert("1/10") == 10
    assert convert("9/10") == 90
    with pytest.raises(ValueError):
        convert("cat/dog")
    with pytest.raises(ZeroDivisionError):
        convert("6/0")

def test_gauge():
    assert gauge(50) == f"{50}%"
    assert gauge(1) == "E"
    assert gauge(99) == "F"