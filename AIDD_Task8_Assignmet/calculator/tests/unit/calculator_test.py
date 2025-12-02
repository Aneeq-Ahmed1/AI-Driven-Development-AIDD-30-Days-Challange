import pytest
from src.calculator import add, subtract, multiply, divide, calculate

def test_add():
    assert add(1, 2) == 3
    assert add(-1, 1) == 0
    assert add(-1, -1) == -2

def test_subtract():
    assert subtract(5, 3) == 2
    assert subtract(3, 5) == -2
    assert subtract(-1, -1) == 0

def test_multiply():
    assert multiply(2, 3) == 6
    assert multiply(-2, 3) == -6
    assert multiply(-2, -3) == 6

def test_divide():
    assert divide(6, 3) == 2
    assert divide(5, 2) == 2.5
    with pytest.raises(ValueError, match="Division by zero"):
        divide(1, 0)

def test_calculate_basic_operations():
    assert calculate("1 + 2") == 3
    assert calculate("5 - 3") == 2
    assert calculate("2 * 3") == 6
    assert calculate("6 / 3") == 2
    assert calculate("5 / 2") == 2.5

def test_calculate_with_parentheses():
    assert calculate("(1 + 2) * 3") == 9
    assert calculate("1 + (2 * 3)") == 7
    assert calculate("(10 - 2) / 4") == 2

def test_calculate_with_decimals():
    assert calculate("1.5 + 2.5") == 4.0
    assert calculate("4.0 * 2.5") == 10.0

def test_calculate_division_by_zero():
    with pytest.raises(ValueError, match="Division by zero"):
        calculate("1 / 0")
    with pytest.raises(ValueError, match="Division by zero"):
        calculate("10 / (5 - 5)")

def test_calculate_invalid_input():
    with pytest.raises(ValueError, match="Invalid characters in expression"):
        calculate("1 & 2")
    with pytest.raises(ValueError, match="Unknown token"):
        calculate("1 plus 2")

def test_calculate_mismatched_parentheses():
    with pytest.raises(ValueError, match="Mismatched parentheses"):
        calculate("(1 + 2")
    with pytest.raises(ValueError, match="Mismatched parentheses"):
        calculate("1 + 2)")
