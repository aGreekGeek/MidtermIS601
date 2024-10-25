import pandas as pd
from typing import List
from app.calculator.calculation import Calculation

class CalculationHistory:
    '''Maintains a record of all calculations performed.'''
    # Static variable to store calculation history as a Pandas DataFrame.
    history: pd.DataFrame = pd.DataFrame(columns=["Operand1", "Operand2", "Operation", "Result"])

    @classmethod
    def add_calculation(cls, calculation: Calculation):
        '''Logs a new calculation into the history DataFrame.'''
        data = {
            "Operand1": calculation.a,
            "Operand2": calculation.b,
            "Operation": calculation.operation.__name__,
            "Result": calculation.compute()
        }
        cls.history = pd.concat([cls.history, pd.DataFrame([data])], ignore_index=True)

    @classmethod
    def get_history(cls) -> pd.DataFrame:
        '''Returns the entire log of calculations.'''
        return cls.history

    @classmethod
    def clear_history(cls):
        '''Clears the complete history of calculations.'''
        cls.history = pd.DataFrame(columns=["Operand1", "Operand2", "Operation", "Result"])

    @classmethod
    def delete_record(cls, index: int):
        '''Deletes a specific record from the history.'''
        if 0 <= index < len(cls.history):
            cls.history = cls.history.drop(index).reset_index(drop=True)
        else:
            print("Invalid record number.")

    @classmethod
    def save_history(cls, filename: str = "calculation_history.csv"):
        '''Saves the history DataFrame to a CSV file.'''
        cls.history.to_csv(filename, index=False)
        print(f"History saved to {filename}.")

    @classmethod
    def load_history(cls, filename: str = "calculation_history.csv"):
        '''Loads the history from a CSV file.'''
        try:
            cls.history = pd.read_csv(filename)
            print(f"History loaded from {filename}.")
        except FileNotFoundError:
            print(f"No file named {filename} found.")