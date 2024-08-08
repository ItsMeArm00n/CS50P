from bank import value

def main():
    test_zero()
    test_20()
    test_100()

def test_zero():
    assert value("Hello") == 0
    assert value("Hello, newman") == 0

def test_20():
    assert value("Hey !") == 20
    assert value("How are you") == 20

def test_100():
    assert value("good morning") == 100
    assert value("good evening") == 100
