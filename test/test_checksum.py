from src.checksum import modulo11_checksum


def test_good():
    assert modulo11_checksum("2-266-11156-8")


def test_bad():
    assert not modulo11_checksum("2-266-11156-3")
