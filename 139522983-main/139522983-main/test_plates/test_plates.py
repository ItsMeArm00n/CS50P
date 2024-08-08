from plates import is_valid

def main():
    test_two_letters()
    test_charlen()
    test_middle()
    test_0()
    test_symbols()

def test_two_letters():
    assert is_valid("AA1234")==True
    assert is_valid("2A1223")==False
    assert is_valid("12ABCD")==False

def test_charlen():
    assert is_valid("ABABAB")==True
    assert is_valid("ABCDEFG")== False

def test_middle():
    assert is_valid("AAA222")==True
    assert is_valid("AA222A")== False

def test_0():
    assert is_valid("AA0123")==False
    assert is_valid("123456") == False

def test_symbols():
    assert is_valid("AA.234")==False
    assert is_valid("AA1 34")==False

