from decimal import Decimal

class Operations:
    @staticmethod
    def addition(a: Decimal, b: Decimal) -> Decimal:
        return a + b

    @staticmethod
    def subtraction(a: Decimal, b: Decimal) -> Decimal:
        return a - b

    @staticmethod
    def multiplication(a: Decimal, b: Decimal) -> Decimal:
        return a * b

    @staticmethod
    def division(a: Decimal, b: Decimal) -> Decimal:
        if b == 0:
            raise ValueError("Division by zero is not allowed.")
        return a / b