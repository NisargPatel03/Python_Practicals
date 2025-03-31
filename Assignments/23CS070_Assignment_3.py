# Write a program to create a basic calculator with functions for addition, subtraction, multiplication, and division.
# Function for Addition
def add(x, y):
    return x + y

# Function for Subtraction
def subtract(x, y):
    return x - y

# Function for Multiplication
def multiply(x, y):
    return x * y

# Function for Division
def divide(x, y):
    if y == 0:
        return "Error! Division by zero."
    return x / y

# Main function to operate the calculator
def calculator():
    print("Select operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")

    # Take user input
    choice = input("Enter choice (1/2/3/4): ")

    # Check if input is valid
    if choice in ['1', '2', '3', '4']:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if choice == '1':
            print(f"The result is: {add(num1, num2)}")
        elif choice == '2':
            print(f"The result is: {subtract(num1, num2)}")
        elif choice == '3':
            print(f"The result is: {multiply(num1, num2)}")
        elif choice == '4':
            print(f"The result is: {divide(num1, num2)}")
    else:
        print("Invalid input! Please choose a valid operation.")

# Running the calculator program
calculator()
print("\n")


# Write a recursive function to calculate the factorial of a number.
def factorial(n):
    # Base case: factorial of 0 or 1 is 1
    if n == 0 or n == 1:
        return 1
    else:
        # Recursive case: n * factorial of (n-1)
        return n * factorial(n - 1)

# Example usage
number = int(input("Enter a number to calculate its factorial: "))
result = factorial(number)
print(f"The factorial of {number} is {result}")
print("\n")


# Write functions to perform various list operations such as finding the maximum, minimum, sum, and average of a list of numbers.
# Function to find the maximum number in a list
def find_max(numbers):
    return max(numbers)

# Function to find the minimum number in a list
def find_min(numbers):
    return min(numbers)

# Function to calculate the sum of all numbers in a list
def find_sum(numbers):
    return sum(numbers)

# Function to calculate the average of the numbers in a list
def find_average(numbers):
    return sum(numbers) / len(numbers) if numbers else 0  # To handle division by zero for empty lists

# Example usage:
numbers = [10, 20, 30, 40, 50]

print(f"Maximum number: {find_max(numbers)}")
print(f"Minimum number: {find_min(numbers)}")
print(f"Sum of numbers: {find_sum(numbers)}")
print(f"Average of numbers: {find_average(numbers)}")
print("\n")


# Write a function that generates the Fibonacci sequence up to a given number of terms using a for loop.
def fibonacci(n):
    # Create an empty list to store the Fibonacci sequence
    fib_sequence = []

    # Handle the first two terms explicitly
    a, b = 0, 1

    for _ in range(n):
        fib_sequence.append(a)  # Add the current value of 'a' to the sequence
        a, b = b, a + b  # Update 'a' and 'b' to the next two terms in the sequence

    return fib_sequence

# Example usage
terms = int(input("Enter the number of terms for the Fibonacci sequence: "))
sequence = fibonacci(terms)
print(f"The Fibonacci sequence up to {terms} terms is: {sequence}")
print("\n")


# Write functions to add, update, and delete key-value pairs in a dictionary, merge two dictionaries, and display the dictionary contents using loops.
def add_key_value(dictionary, key, value):
    dictionary[key] = value
    print(f"Added: {key} = {value}")

def update_key_value(dictionary, key, value):
    if key in dictionary:
        dictionary[key] = value
        print(f"Updated: {key} = {value}")
    else:
        print(f"Key '{key}' not found.")

def delete_key_value(dictionary, key):
    if key in dictionary:
        del dictionary[key]
        print(f"Deleted: {key}")
    else:
        print(f"Key '{key}' not found.")

def merge_dictionaries(dict1, dict2):
    dict1.update(dict2)
    print(f"Merged dictionary: {dict1}")

def display_dictionary(dictionary):
    print("Dictionary contents:")
    for key, value in dictionary.items():
        print(f"{key}: {value}")

# Create a dictionary
my_dict = {"name": "Alice", "age": 25, "city": "New York"}

# Add a key-value pair
add_key_value(my_dict, "job", "Engineer")

# Update a key-value pair
update_key_value(my_dict, "age", 26)

# Delete a key-value pair
delete_key_value(my_dict, "city")

# Merge with another dictionary
new_dict = {"country": "USA", "hobby": "Reading"}
merge_dictionaries(my_dict, new_dict)

# Display the dictionary contents
display_dictionary(my_dict)
print("\n")


# Write a program to create a simple to-do list application that allows users to add, remove, and view tasks.
# To-Do List Application

# Initialize an empty list to store tasks
tasks = []

# Function to add a task
def add_task(task):
    tasks.append(task)
    print(f"Task added: {task}")

# Function to remove a task by its index
def remove_task(task_index):
    if 0 <= task_index < len(tasks):
        removed_task = tasks.pop(task_index)
        print(f"Task removed: {removed_task}")
    else:
        print("Invalid task index.")

# Function to view all tasks
def view_tasks():
    if tasks:
        print("Your To-Do List:")
        for idx, task in enumerate(tasks, 1):
            print(f"{idx}. {task}")
    else:
        print("Your To-Do list is empty.")

# Function to display the menu
def display_menu():
    print("\nTo-Do List Menu:")
    print("1. Add Task")
    print("2. Remove Task")
    print("3. View Tasks")
    print("4. Exit")

# Main program loop
def main():
    while True:
        display_menu()
        choice = input("Choose an option (1/2/3/4): ")

        if choice == '1':
            task = input("Enter a task to add: ")
            add_task(task)
        elif choice == '2':
            view_tasks()
            try:
                task_index = int(input("Enter the task number to remove: ")) - 1
                remove_task(task_index)
            except ValueError:
                print("Invalid input. Please enter a valid task number.")
        elif choice == '3':
            view_tasks()
        elif choice == '4':
            print("Exiting the To-Do List Application. Goodbye!")
            break
        else:
            print("Invalid option. Please try again.")

# Run the program
if __name__ == "__main__":
    main()

print("\n")


# Write a program that accepts a list of numbers and returns a new list containing only the even numbers.
def filter_even_numbers(numbers):
    # Use list comprehension to filter even numbers
    even_numbers = [num for num in numbers if num % 2 == 0]
    return even_numbers

# Example usage:
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers = filter_even_numbers(numbers)
print("Even numbers:", even_numbers)
print("\n")


# Write a program that finds the largest and smallest numbers in a list without using built-in functions like max() and min().
def find_largest_and_smallest(numbers):
    # Initialize the largest and smallest numbers
    largest = numbers[0]
    smallest = numbers[0]

    # Iterate through the list to compare each number
    for num in numbers:
        if num > largest:
            largest = num
        if num < smallest:
            smallest = num

    return largest, smallest

# Example usage:
numbers = [10, 3, 45, 7, 8, 23, 90, 2]
largest, smallest = find_largest_and_smallest(numbers)
print(f"Largest number: {largest}")
print(f"Smallest number: {smallest}")
print("\n")