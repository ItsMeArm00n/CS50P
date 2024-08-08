from fuel import convert, gauge
import pytest

def main():
    pass

def test_div_0():
    with pytest.raises(ZeroDivisionError):
        convert("1/0")

def test_div_strr():
    with pytest.raises(ValueError):
        convert("cat/dog")

def test_output():
    assert convert("100/100")== 100 and gauge(100)=="F"
    assert convert("1/100")== 1 and gauge(1)=="E"
    assert convert("99/100")== 99 and gauge(99)=="F"
    assert convert("25/100")== 25 and gauge(25)=="25%"
