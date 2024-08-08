from um import count

def test():
    assert count("Hello, um, world") == 1
    assert count("um um um um um ") == 5
    assert count("Um? Mum? Is this that album where, um, umm, the clumsy alums play drums?") == 2
    assert count("Um, thanks, um, regular expressions make sense now") == 2
    assert count("yummy") ==0
    assert count("UM UM UM UM UM") == 5
