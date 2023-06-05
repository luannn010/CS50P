from bank import value


def test_noCaseSensitive():
    assert value("HelLo") == 0
    assert value("WHAT'S UP!") == 100
    assert value("Hi!") == 20
    assert value("彡ᕕ(´•‿‿•`)ง彡") == 100
