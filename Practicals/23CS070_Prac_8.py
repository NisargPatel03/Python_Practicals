# 1. Use a try-except block to catch and handle exceptions
try:
    num = int(input("Enter a number: "))
    result = 100 / num
    print("Result:", result)
except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")
except ValueError:
    print("Error: Invalid input! Please enter a number.")

# 2. Use multiple except blocks to handle different types of exceptions
try:
    values = [10, 20, 30]
    index = int(input("\nEnter an index (0-2): "))
    print("Value at index:", values[index])
except IndexError:
    print("Error: Index out of range!")
except ValueError:
    print("Error: Invalid input! Please enter a valid integer index.")

# 3. Use an else block to execute code if no exceptions are raised
try:
    age = int(input("\nEnter your age: "))
except ValueError:
    print("Error: Please enter a valid number!")
else:
    print("You entered a valid age:", age)

# 4. Use a finally block to execute code regardless of exceptions
try:
    print("\nOpening file...")
    file = open("example.txt", "w")
    file.write("This is a sample text.")
except Exception as e:
    print("Error occurred:", e)
finally:
    file.close()
    print("File closed.")

# 5. Use the raise statement to raise an exception manually
def check_positive(num):
    if num < 0:
        raise ValueError("Negative numbers are not allowed!")
    return num

try:
    value = int(input("\nEnter a positive number: "))
    print("Valid number:", check_positive(value))
except ValueError as e:
    print("Custom Error:", e)
