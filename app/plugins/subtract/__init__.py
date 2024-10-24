from app.commands import Command
from app.calculator import Calculator
from app.utils.validation import validate_decimal_input

class SubtractCommand(Command):
    '''Handles the subtraction command within the application.'''

    def execute(self):
        '''
        Executes the subtraction process.

        Requests two numeric inputs from the user, performs the subtraction,
        and displays the resulting value.
        '''
        num1 = validate_decimal_input("Please enter the first number: ")
        num2 = validate_decimal_input("Please enter the second number: ")
        result = Calculator.subtract(num1, num2)
        print(f"The result of subtracting {num2} from {num1} is: {result}")
        return result
