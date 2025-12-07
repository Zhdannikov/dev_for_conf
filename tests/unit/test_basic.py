def test_basic_math():
    assert 1 + 1 == 2

def test_string_operations():
    name = "conference"
    assert len(name) == 10
    assert name.upper() == "CONFERENCE"