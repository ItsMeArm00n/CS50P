import pytest
from jar import Jar
jar=Jar()
def test_deposit():
    jar.deposit(1)
    assert str(jar) == "🍪"

def test_dep_error():
    jar.deposit(1)
    assert str(jar) == "🍪🍪"
    with pytest.raises(ValueError):
        jar.deposit(100)

def test_withdraw():
    jar.deposit(10)
    assert str(jar) == "🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪"
    jar.withdraw(5)
    assert str(jar) == "🍪🍪🍪🍪🍪🍪🍪"


def test_withdraw_error():
    jar.deposit(1)
    assert str(jar) == "🍪🍪🍪🍪🍪🍪🍪🍪"
    with pytest.raises(ValueError):
        jar.withdraw(100)

