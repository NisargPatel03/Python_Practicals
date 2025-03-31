# 1. Define a custom exception and raise it in specific scenarios
class CustomError(Exception):
    """Custom Exception for specific scenarios."""
    pass

def check_value(value):
    if value < 0:
        raise CustomError("Negative values are not allowed!")
    else:
        print("Valid value:", value)

try:
    num = int(input("Enter a positive number: "))
    check_value(num)
except CustomError as e:
    print("Custom Exception Caught:", e)

# 2. Access an element in a list and handle IndexError
numbers = [10, 20, 30, 40, 50]

try:
    index = int(input("\nEnter an index to access (0-4): "))
    print("Element at index", index, ":", numbers[index])
except IndexError:
    print("Error: Index out of range! Please enter a valid index (0-4).")
except ValueError:
    print("Error: Please enter a valid integer index.")

# 3. Convert a string to an integer and handle ValueError
while True:
    try:
        user_input = input("\nEnter a number: ")
        number = int(user_input)
        print("Valid number:", number)
        break
    except ValueError:
        print("Error: Invalid input! Please enter a valid integer.")
