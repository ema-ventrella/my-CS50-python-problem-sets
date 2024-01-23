import pytest
from seasons.seasons import cal
from datetime import date

def test_same_date():
    today = date(1990, 1, 1)
    assert cal("1990-01-01", today) == "Zero minutes"
    
def test_one_day():
    today = date(2011, 1, 1)
    assert cal("1990-01-01", today) == "Eleven million, forty-four thousand, eight hundred minutes"
    
def test_nope():
    with pytest.raises(SystemExit):
        cal("Nope.", date.today()) == "Invalid date"
        cal(1234, date.today()) == "Invalid date"
