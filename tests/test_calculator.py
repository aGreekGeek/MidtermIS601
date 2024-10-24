'''Test File: app/calculator/__init__.py'''
# Disable specific pylint warnings that are irrelevant to this test file.
# pylint: disable=unnecessary-dunder-call, invalid-name
import pytest
from app.calculator import Calculator

def test_calculator_operations(a, b, operation, expected):
    '''Tests the _perform_calculations method of the Calculator class.'''
    assert operation(a, b) == expected, f"Operation {operation.__name__} failed with inputs {a} and {b}"

def test_addition():
    '''Ensure that the add function of Calculator behaves correctly.'''
    assert Calculator.add(2, 2) == 4

def test_subtraction():
    '''Verify that the subtract function of Calculator works as expected.'''
    assert Calculator.subtract(2, 2) == 0

def test_multiply():
    '''Confirm that the multiply function of Calculator returns correct results.'''
    assert Calculator.multiply(2, 2) == 4

def test_divide():
    '''Check if the divide function of Calculator handles division correctly.'''
    assert Calculator.divide(2, 2) == 1

def test_calculator_divide_by_zero():
    '''Test that dividing by zero raises the appropriate exception.'''
    with pytest.raises(ValueError):
        Calculator.divide(2, 0)
