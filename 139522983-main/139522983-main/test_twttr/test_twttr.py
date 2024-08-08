from twttr import shorten

def main():
    test_lower()
    test_upper()
    test_upper_lower()
    test_number()
    test_punctuation()

def test_lower():
    assert shorten("twitter") == "twttr"

def test_upper():
    assert shorten("TWITTER") == "TWTTR"

def test_upper_lower():
    assert shorten("TwItTeR") =="TwtTR"

def test_number():
    assert shorten("50") == "50"
    assert shorten("This is CS50") == "Ths s CS50"

def test_punctuation():
    assert shorten("?,!")
