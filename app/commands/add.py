from app.commands import Command
from app.strategies import add_strategy
from app.utils.validation import validate_decimal_input

class AddCommand(Command):
    '''Command class to perform addition operation.'''

    def execute(self):
        num1 = validate_decimal_input("Enter the first number: ")
        num2 = validate_decimal_input("Enter the second number: ")
        result = add_strategy(num1, num2)
        print(f"The result of {num1} + {num2} is: {result}")