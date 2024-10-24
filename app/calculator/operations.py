'''operation.py: Implements basic arithmetic operations such as addition, subtraction, multiplication, and division.'''
from decimal import Decimal  # Import Decimal to handle precise arithmetic

class Operations:
    '''Class providing fundamental arithmetic operations.'''

    @staticmethod
    def addition(a: Decimal, b: Decimal) -> Decimal:
        '''Performs addition of two numbers and returns the result.'''
        return a + b

    @staticmethod
    def subtraction(a: Decimal, b: Decimal) -> Decimal:
        '''Performs subtraction of two numbers and returns the result.'''
        return a - b

    @staticmethod
    def multiplication(a: Decimal, b: Decimal) -> Decimal:
        '''Performs multiplication of two numbers and returns the result.'''
        return a * b

    @staticmethod
    def division(a: Decimal, b: Decimal) -> Decimal:
        '''Performs division of two numbers and handles division by zero.'''
        if b == 0:
            raise ValueError("Division by zero is not allowed.")
        return a / b