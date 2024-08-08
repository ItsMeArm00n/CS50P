from numb3rs import validate

def test():
    assert validate(r"0.0.0.0") == True
    assert validate(r"255.255.255.255") == True
    assert validate(r"235.23.246.75") == True
    assert validate(r"0.0.0.0.0") == False
    assert validate(r"0,0,0,0") == False
    assert validate(r"300.342.235.53") == False
    assert validate(r"cs50") == False
    assert validate(r"512.512.512.512.512") == False
    assert validate(r"192.168.1.256") == False
