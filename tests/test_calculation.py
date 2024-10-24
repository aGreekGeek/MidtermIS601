'''Test File: app/calculator/calculation.py'''
# Disable specific pylint warnings that are not relevant to this test file.
# pylint: disable=unnecessary-dunder-call, invalid-name
from decimal import Decimal
import pytest
from app.calculator.calculation import Calculation
from app.calculator.operations import Operations as op

def test_calculation_operations(a, b, operation, expected):
    '''Test the compute method for different calculation operations.'''
    calc = Calculation.create_calculation(a, b, operation)
    assert calc.compute() == expected, f"Operation {operation.__name__} failed with inputs {a} and {b}"

def test_calculation_divide_by_zero():
    '''Checks that a division by zero raises the correct exception.'''
    with pytest.raises(ValueError):
        calc = Calculation(Decimal('5'), Decimal('0'), op.division)
        calc.compute()

def test_calculation_string_representation():
    '''Test the string representation of the Calculation class to ensure accuracy.'''
    str_rep = Calculation.create_calculation(Decimal('10'), Decimal('5'), op.addition)
    expected_rep = "Calculation(10, 5, addition)"
    assert str_rep.__repr__() == expected_rep, "The __repr__ output does not match the expected value."
