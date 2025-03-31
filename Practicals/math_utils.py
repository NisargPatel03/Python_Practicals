# math_utils.py
def basic_arithmetic(num1, num2, operation):
    """Perform basic arithmetic operations"""
    if operation == 'add':
        return num1 + num2
    elif operation == 'subtract':
        return num1 - num2
    elif operation == 'multiply':
        return num1 * num2
    elif operation == 'divide':
        if num2 != 0:
            return num1 / num2
        else:
            return "Cannot divide by zero"
    else:
        return "Invalid operation"

def is_even_or_odd(number):
    """Check if a number is even or odd"""
    if number % 2 == 0:
        return "Even"
    else:
        return "Odd"