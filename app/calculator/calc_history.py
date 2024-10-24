'''calc_history.py: Responsible for handling calculation history, providing methods for adding, retrieving, and clearing records.'''
from typing import List
from app.calculator.calculation import Calculation

class CalculationHistory:
    '''Maintains a record of all calculations performed.'''
    # Static variable to store the list of 'Calculation' instances.
    history: List[Calculation] = []

    @classmethod
    def add_calculation(cls, calculation: Calculation):
        '''Logs a new calculation into the history by appending a 'Calculation' instance.'''
        cls.history.append(calculation)

    @classmethod
    def get_history(cls) -> List[Calculation]:
        '''Returns the entire log of calculations.'''
        return cls.history

    @classmethod
    def clear_history(cls):
        '''Clears the complete history of calculations.'''
        cls.history.clear()

    @classmethod
    def get_lastest_history(cls):
        '''Returns the most recent calculation if available, otherwise None.'''
        if cls.history:
            return cls.history[-1]
        return None