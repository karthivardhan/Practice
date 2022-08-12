import pytest

@pytest.fixture()
def setUp():
    print("Once before every method")
    yield
    print("Once after every method")

def test_methodA(setUp):
    print("Method A")

def test_methodB(setUp):
    print("Method B")