import os
import sys

# Add the parent directory (project root) to the Python path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from calculator import add

def test_add_positive_numbers():
    assert add(2, 3) == 5

def test_add_zero():
    assert add(0, 0) == 0

def test_add_negative_numbers():
    assert add(-2, -3) == -5
