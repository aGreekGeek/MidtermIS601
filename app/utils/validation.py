'''utils/validation.py: Defines a function to validate user input as a Decimal number.'''
from decimal import Decimal, InvalidOperation

def validate_decimal_input(prompt):
    '''
    Prompts the user for input and validates it as a Decimal number.

    Continues prompting the user until a valid Decimal is entered.

    Args:
        prompt (str): The message displayed to the user asking for input.

    Returns:
        Decimal: The validated Decimal number entered by the user.
    '''
    while True:
        user_input = input(prompt)
        try:
            validated_num = Decimal(user_input)  # Try converting the input to a Decimal
            return validated_num
        except InvalidOperation:
            print("Invalid input. Please enter a valid number.")  # Error message for invalid input
