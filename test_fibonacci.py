#Pair Nagawa Esther and Aloyo Brenda
import pytest
from fibonacci import fibonacci

# Test Fibonacci for 0
def test_fibonacci_zero():
    assert fibonacci(0) == 0

# Test Fibonacci for 1
def test_fibonacci_one():
    assert fibonacci(1) == 1

# Test Fibonacci for 2
def test_fibonacci_two():
    assert fibonacci(2) == 1

# Test Fibonacci for 3
def test_fibonacci_three():
    assert fibonacci(3) == 2

# Test Fibonacci for 5
def test_fibonacci_five():
    assert fibonacci(5) == 5

# Test Fibonacci for 10
def test_fibonacci_ten():
    assert fibonacci(10) == 55

# Test negative input raises error
def test_negative_number():
    with pytest.raises(ValueError):
        fibonacci(-1)
