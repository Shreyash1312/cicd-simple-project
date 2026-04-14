from src.calculator import add, subract

def test_add():
  assert add(2,3) == 5

def test_subtract():
  assert subract(5,3) == 2