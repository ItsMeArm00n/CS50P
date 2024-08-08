from seasons import convert


def test_main():
    assert convert(r"2008-12-27") == (r"Eight million, one hundred ninety-nine thousand, three hundred sixty minutes")
    assert convert(r"1999-01-01") == (r"Thirteen million, four hundred fifty-two thousand, four hundred eighty minutes")

