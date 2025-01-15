from src.main import add

def test_add():
    assert add(3,5) == 8
    assert add(0,0) == 0