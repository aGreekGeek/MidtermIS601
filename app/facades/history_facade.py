import pandas as pd
from app.calculator.calc_history import CalculationHistory

class HistoryFacade:
    '''Facade to simplify interaction with calculation history.'''

    @staticmethod
    def add_to_history(a, b, operation):
        '''Add a new calculation to the history.'''
        from app.calculator.calculation import Calculation  # Lazy import to avoid circular dependency
        calc = Calculation(a, b, operation)
        CalculationHistory.add_calculation(calc)

    @staticmethod
    def save_history(filename: str = "calculation_history.csv"):
        '''Save history to a CSV file.'''
        CalculationHistory.save_history(filename)

    @staticmethod
    def load_history(filename: str = "calculation_history.csv"):
        '''Load history from a CSV file.'''
        CalculationHistory.load_history(filename)

    @staticmethod
    def clear_history():
        '''Clear the entire calculation history.'''
        CalculationHistory.clear_history()

    @staticmethod
    def get_full_history() -> pd.DataFrame:
        '''Retrieve the full calculation history.'''
        return CalculationHistory.get_history()

    @staticmethod
    def delete_history_record(index: int):
        '''Delete a specific record from the history.'''
        CalculationHistory.delete_record(index)

    @staticmethod
    def sort_history(by: str = "Operation", ascending: bool = True) -> pd.DataFrame:
        '''Sort the calculation history by a given column.'''
        return CalculationHistory.sort_history(by, ascending)

    @staticmethod
    def filter_history(operation: str) -> pd.DataFrame:
        '''Filter the calculation history by operation type.'''
        return CalculationHistory.filter_history(operation)