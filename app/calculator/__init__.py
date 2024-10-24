'''__init__.py: Module responsible for bringing together different parts of the calculator. 
Defines a class to handle arithmetic operations and keep track of calculation history.'''

from decimal import Decimal
from typing import Callable
from app.calculator.calculation import Calculation
from app.calculator.operations import Operations as ops
from app.calculator.calc_history import CalculationHistory as history

class Calculator:
    '''Core class for basic arithmetic operations and maintaining history of performed calculations.'''

    @staticmethod
    def _execute_operation(a: Decimal, b: Decimal, operation: Callable[[Decimal, Decimal], Decimal]) -> Decimal:
        '''Handles performing a calculation and storing it in the history. Returns the result.'''
        calculation_instance = Calculation.create_calculation(a, b, operation)
        history.add_calculation(calculation_instance)
        return calculation_instance.compute()

    @staticmethod
    def add(a: Decimal, b: Decimal) -> Decimal:
        '''Performs addition by calling the execute operation method.'''
        return Calculator._execute_operation(a, b, ops.addition)

    @staticmethod
    def subtract(a: Decimal, b: Decimal) -> Decimal:
        '''Performs subtraction by calling the execute operation method.'''
        return Calculator._execute_operation(a, b, ops.subtraction)

    @staticmethod
    def multiply(a: Decimal, b: Decimal) -> Decimal:
        '''Performs multiplication by calling the execute operation method.'''
        return Calculator._execute_operation(a, b, ops.multiplication)

    @staticmethod
    def divide(a: Decimal, b: Decimal) -> Decimal:
        '''Performs division by calling the execute operation method.'''
        return Calculator._execute_operation(a, b, ops.division)
