# BASICS OF FUNCTIONS
# Define a simple function that takes inputs and returns an output.
def my_function(input_value):
  return input_value

output = my_function(70)
print(output)

output = my_function('CSPIT CHARUSAT')
print(output)
print("\n")


# Define a function with positional, keyword, default, and variable-length arguments
def example_function(pos_arg, /, default_arg="default", *var_args, kw_only, **kw_args):
    """
    Demonstrates positional, default, variable-length, and keyword-only arguments.

    :param pos_arg: A required positional argument.
    :param default_arg: A positional-or-keyword argument with a default value.
    :param var_args: Captures additional positional arguments.
    :param kw_only: A keyword-only argument (must be passed by name).
    :param kw_args: Captures additional keyword arguments.
    """
    print(f"Positional argument: {pos_arg}")
    print(f"Default argument: {default_arg}")
    print(f"Variable positional arguments: {var_args}")
    print(f"Keyword-only argument: {kw_only}")
    print(f"Additional keyword arguments: {kw_args}")


example_function(1, "custom", 2, 3, 4, kw_only="required_kw", extra="extra_kw")
print("\n")


# Define a function that returns the multiple values using tuple.
def my_function(input_value):
  square = input_value ** 2
  cube = input_value ** 3
  return (input_value, square, cube)


result = my_function(5)
print(result)
print(type(result))
print("\n")


# Define an anonymous function using lamba keyword
square = lambda x: x**2

result = square(70)
print(result)
print("\n")


# Define a function inside another function.
def outer_function(x):

  def inner_function(y):
    return x + y

  return inner_function

# Example usage:
my_function = outer_function(10)
result = my_function(5)
print(result)
print("\n")


# Create and use decorators to modify the behavior of functions.
import time
import functools

def timer(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"Function {func.__name__} took {end_time - start_time:.4f} seconds to execute.")
        return result
    return wrapper

@timer
def slow_function():
    time.sleep(2)

slow_function()
print("\n")


# Define a function that calls itself to solve a problem recursively.
def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

result = fibonacci(6)
print(result)
print("\n")


# Define functions that take other functions as arguments or return functions as results.
# Function as Argument

def apply_function(func, value):

    return func(value)

def square(x):
    return x * x

result = apply_function(square, 5)
print(result)
print("\n")

# Function as return value

def create_adder(x):
    def adder(y):
        return x + y
    return adder

# Example usage:
add_5 = create_adder(5)  # add_5 is now a function
result = add_5(10)
print(result)  # Output: 15

# Add docstrings to functions to document their purpose and usage.
import functools

def my_decorator(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print("Something is happening before the function is called.")
        result = func(*args, **kwargs)
        print("Something is happening after the function is called.")
        return result
    return wrapper

@my_decorator
def say_hello(name):
    """This function prints a greeting."""
    print(f"Hello, {name}!")

say_hello("World")
print("\n")


# Use type annotations to specify the expected types of function arguments and return values.
from typing import Any

def example_function(
    pos_arg: int, /,
    default_arg: str = "default",
    *var_args: float,
    kw_only: bool,
    **kw_args: Any
) -> None:
    print(f"Positional argument: {pos_arg}")
    print(f"Default argument: {default_arg}")
    print(f"Variable positional arguments: {var_args}")
    print(f"Keyword-only argument: {kw_only}")
    print(f"Additional keyword arguments: {kw_args}")

# Example usage:
example_function(1, "custom", 2.5, 3.7, kw_only=True, extra="extra_kw")
print("\n")



# BASICS OF LOOPS
# Iterate over a sequence (list, tuple, string, or range) using a for loop.
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)


text = "hello"
for char in text:
    print(char)


numbers = (10, 20, 30)
for num in numbers:
    print(num)


for i in range(5):
    print(i)
print("\n")


# Repeat a block of code as long as a condition is true using a while loop.
count = 0
while count < 5:
    print(f"Count is {count}")
    count += 1
print("\n")


# Use loops inside other loops to handle multi-dimensional data structures.
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

for row in matrix:
    for value in row:
        print(value, end=" ")
    print()

print("\n")


# Use break, continue, and pass to control the flow of loops.
for num in range(1, 10):
    if num == 5:
        print("Stopping at", num)
        break  # Exits the loop when num is 5
    print(num)


for num in range(1, 6):
    if num == 3:
        print("Skipping", num)
        continue  # Skips printing 3
    print(num)


for num in range(1, 6):
    if num == 3:
        pass  # Placeholder for future logic
    else:
        print(num)
    

print("\n")


# Use the enumerate function to get both the index and value while iterating over a sequence.
fruits = ["apple", "banana", "cherry"]

for index, fruit in enumerate(fruits):
    print(f"Index: {index}, Fruit: {fruit}")

print("\n")


# Use the range function to generate a sequence of numbers for iteration.
for num in range(5):  # Generates 0, 1, 2, 3, 4
    print(num)

print("\n")


# Iterate over the key-value pairs of a dictionary using a for loop.
student_scores = {"Alice": 85, "Bob": 90, "Charlie": 78}

for value in student_scores.values():
    print(f"Score: {value}")

student_scores = {"Alice": 85, "Bob": 90, "Charlie": 78}

for key, value in student_scores.items():
    print(f"Student: {key}, Score: {value}")

print("\n")


# Use list comprehensions to create new lists by applying an expression to each item in an existing list.
numbers = [1, 2, 3, 4, 5]
squares = [num ** 2 for num in numbers]
print(squares)
print("\n")