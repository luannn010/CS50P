from ProblemSet5.twttr.twttr import shorten


def main():
    test_uppercase()
    test_lowercase()
    test_allvowels()
    test_number()
    test_specialchar()

def test_uppercase():
    assert shorten("YOUTUBE") == "YTB"
def test_lowercase():
    assert shorten("friend") == "frnd"
def test_allvowels():
    assert shorten("aieuo") == ""
def test_number():
    assert shorten("a1i2u3") =="123"
def test_specialchar():
    assert shorten("Hello, World") == "Hll, Wrld"


if __name__ == "__main__":
    main()

