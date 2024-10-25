from app.commands import CommandHandler
from app.calculator import Calculator
from app.utils.validation import validate_decimal_input
from app.commands import Command

class AddCommand(Command):
    '''A command class to perform addition.'''

    def execute(self):
        '''
        Execute the AddCommand.

        This method prompts the user to enter two numbers and performs addition.
        '''
        num1 = validate_decimal_input("Enter the first number: ")
        num2 = validate_decimal_input("Enter the second number: ")
        result = Calculator.add(num1, num2)
        print(f"The result of {num1} + {num2} is: {result}")
        return result

def register_commands(handler: CommandHandler):
    '''Registers AddCommand with the command handler.'''
    handler.register_command('add', AddCommand())