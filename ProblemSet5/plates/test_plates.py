from plates import is_valid

def main():
    test_BeginWith2Letters()
    test_Maximum()
    test_Minimum()
    test_NoNumInTheMiddle()
    test_DontStartWithZero()
    test_NoPunctualMark()


def test_BeginWith2Letters():
    assert is_valid("CS") == True
    assert is_valid("50") == False
    assert is_valid("C5") == False
    assert is_valid("5") == False

def test_Maximum():
    assert is_valid("ABCDEF") == True
    assert is_valid("AVC1234") == False

def test_Minimum():
    assert is_valid("CS") == True
    assert  is_valid("C") == False

def test_NoNumInTheMiddle():
    assert is_valid("CS50P") == False

def test_DontStartWithZero():
    assert is_valid("CS05") == False

def test_NoPunctualMark():
    assert  is_valid("CS50!") == False


if __name__ == "__main__":
    main()