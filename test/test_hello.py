from hello import hello


def test_default():
    assert hello() == "hello world"


def test_arg():
    assert hello("david") == "hello david"
