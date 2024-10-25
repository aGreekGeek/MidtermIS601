from app.commands import Command
from app.calculator import Calculator
from app.utils.validation import validate_decimal_input
from app.commands import CommandHandler
from app.plugins.add import AddCommand

class MultiplyCommand(Command):
    '''Command class for handling multiplication operations.'''

    def execute(self):
        '''
        Executes the MultiplyCommand.

        Prompts the user for two input numbers, performs multiplication,
        and prints the result.
        '''
        num1 = validate_decimal_input("Enter the first number: ")
        num2 = validate_decimal_input("Enter the second number: ")
        result = Calculator.multiply(num1, num2)
        print(f"The product of {num1} and {num2} is: {result}")
        return result

def register_commands(handler: CommandHandler):
    '''Registers AddCommand with the command handler.'''
    handler.register_command('multiply', MultiplyCommand())
