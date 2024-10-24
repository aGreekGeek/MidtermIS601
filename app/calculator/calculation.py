'''calculation.py: Represents a single calculation, providing abstraction for handling operations within the Calculator class.'''
from decimal import Decimal
from typing import Callable

class Calculation:
    '''Represents an individual calculation and encapsulates its logic.'''

    def __init__(self, a: Decimal, b: Decimal, operation: Callable[[Decimal, Decimal], Decimal]) -> None:
        '''Initializes a calculation object with two operands and an operation to perform.'''
        self.a = a
        self.b = b
        self.operation = operation

    @staticmethod
    def create_calculation(a: Decimal, b: Decimal, operation: Callable[[Decimal, Decimal], Decimal]):
        '''Factory method for generating new Calculation objects without explicitly invoking the constructor.'''
        return Calculation(a, b, operation)

    def compute(self):
        '''Executes the operation with the provided operands and returns the result.'''
        return self.operation(self.a, self.b)

    def __repr__(self):
        '''Provides a string representation of the calculation, showing the operands and operation name.'''
        return f"Calculation({self.a}, {self.b}, {self.operation.__name__})"