from decimal import Decimal
from app.calculator.operations import Operations

# Strategy functions that wrap existing methods
def add_strategy(a: Decimal, b: Decimal) -> Decimal:
    return Operations.addition(a, b)

def subtract_strategy(a: Decimal, b: Decimal) -> Decimal:
    return Operations.subtraction(a, b)

def multiply_strategy(a: Decimal, b: Decimal) -> Decimal:
    return Operations.multiplication(a, b)

def divide_strategy(a: Decimal, b: Decimal) -> Decimal:
    return Operations.division(a, b)