from hello import hello

def test_default():
    assert hello() == "hello, world"

def test_argument():
    for name in["Arman", "Farhan", "Imran", "Rehan"]:
        assert hello(name) == f"hello, {name}"

def  test_argument():
    assert hello("Arman") == "hello, Arman"



