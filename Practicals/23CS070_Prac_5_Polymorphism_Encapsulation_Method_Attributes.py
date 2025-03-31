# Write a program to demonstrate polymorphism by defining a common interface and implementing it in multiple classes..

from abc import ABC, abstractmethod

# Define a common interface (abstract class)
class Animal(ABC):
    @abstractmethod
    def sound(self):
        pass

# Implement the common interface in multiple classes
class Dog(Animal):
    def sound(self):
        return "Woof"

class Cat(Animal):
    def sound(self):
        return "Meow"

class Cow(Animal):
    def sound(self):
        return "Moo"

# Function to demonstrate polymorphism
def animal_sound(animal: Animal):
    print(animal.sound())

# Testing polymorphism
dog = Dog()
cat = Cat()
cow = Cow()

# Passing different objects to the same function
animal_sound(dog)  
animal_sound(cat)  
animal_sound(cow) 

print("\n")



# Write a program to override methods in a subclass to provide specific implementations.

# Define a base class
class Student:
    def get_status(self):
        return "Generic student status"

# Define a subclass for Undergraduate students that overrides get_status method
class UndergraduateStudent(Student):
    def get_status(self):
        return "Undergraduate student"

# Define a subclass for Graduate students that overrides get_status method
class GraduateStudent(Student):
    def get_status(self):
        return "Graduate student"

# Function to demonstrate method overriding
def print_student_status(student):
    print(student.get_status())

# Testing the method overriding
student = Student()
undergraduate = UndergraduateStudent()
graduate = GraduateStudent()

# Calling the overridden methods
print_student_status(student)         # Output: Generic student status
print_student_status(undergraduate)   # Output: Undergraduate student
print_student_status(graduate)        # Output: Graduate student
print("\n")



# Write a program to define multiple methods with the same name but different parameters to handle different types of inputs.

class MathOperations:
    # Method to add two numbers (handles two integer inputs)
    def add(self, a, b):
        if isinstance(a, int) and isinstance(b, int):
            return a + b
        elif isinstance(a, float) and isinstance(b, float):
            return a + b
        else:
            raise TypeError("Both inputs must be either integers or floats")
    
    # Method to add a list of numbers (handles multiple inputs as a list)
    def add(self, a, b=None):
        if isinstance(a, list):
            return sum(a)
        elif b is not None:
            return a + b
        else:
            raise TypeError("Invalid input. Expected a list or two numbers.")

# Testing the methods
math = MathOperations()

# Adding two integers
print(math.add(10, 5))          # Output: 15

# Adding two floats
print(math.add(3.5, 4.5))       # Output: 8.0

# Adding a list of numbers
print(math.add([1, 2, 3, 4]))   # Output: 10

print("\n")



# Write a program to define class methods using the @classmethod decorator to operate on class-level data.

class Employee:
    # Class-level data (shared among all instances)
    employee_count = 0

    

    def __init__(self, name, position):
        self.name = name
        self.position = position
        Employee.employee_count += 1  # Increment the employee count whenever a new employee is created

    # Class method to get the current employee count
    @classmethod
    def get_employee_count(cls):
        return cls.employee_count

    # Class method to create a new employee using class data
    @classmethod
    def create_employee(cls, name, position):
        return cls(name, position)

# Testing the class methods
emp1 = Employee("John Doe", "Software Engineer")
emp2 = Employee("Jane Smith", "Data Scientist")

# Accessing the class method to get the employee count
print("Employee Count:", Employee.get_employee_count())  # Output: Employee Count: 2

# Using the class method to create a new employee
emp3 = Employee.create_employee("Alice Brown", "Product Manager")
# Checking the employee count after creating another employee
print("Employee Count after adding new employee:", Employee.get_employee_count())  # Output: Employee Count after adding new employee: 3

print("\n")



# Write a program to define static methods using the @staticmethod decorator for utility functions that do not depend on instance or class data.

class MathUtils:
    
    @staticmethod
    def add(a, b):
        return a + b
    
    @staticmethod
    def multiply(a, b):
        return a * b
    
    @staticmethod
    def square(number):
        return number ** 2

# Testing the static methods
print("Addition of 5 and 3:", MathUtils.add(5, 3))       # Output: 8
print("Multiplication of 5 and 3:", MathUtils.multiply(5, 3))  # Output: 15
print("Square of 4:", MathUtils.square(4))                # Output: 16

# Static methods can also be called on instances (although it's not common practice)
math_utils_instance = MathUtils()
print("Addition using instance:", math_utils_instance.add(10, 20))  # Output: 30

print("\n")



# Write a program to Use the @property decorator to create getter and setter methods for attributes.
class Employee:
    def __init__(self, name, salary):  # Fixed __init__ method
        self._name = name
        self._salary = salary

    # Getter for 'name'
    @property
    def name(self):
        return self._name

    # Setter for 'name'
    @name.setter
    def name(self, value):
        if len(value) < 3:
            raise ValueError("Name must be at least 3 characters long.")
        self._name = value

    # Getter for 'salary'
    @property
    def salary(self):
        return self._salary

    # Setter for 'salary'
    @salary.setter
    def salary(self, value):
        if value < 0:
            raise ValueError("Salary cannot be negative.")
        self._salary = value


# Testing the @property decorator
emp = Employee("John Doe", 50000)

# Accessing the attributes using getter methods
print("Name:", emp.name)  # Output: John Doe
print("Salary:", emp.salary)  # Output: 50000

# Modifying the attributes using setter methods
emp.name = "Jane Smith"
emp.salary = 60000

print("Updated Name:", emp.name)  # Output: Jane Smith
print("Updated Salary:", emp.salary)  # Output: 60000

# Attempting to set invalid values (this will raise an exception)
try:
    emp.name = "Jo"  # Name too short
except ValueError as e:
    print(e)  # Output: Name must be at least 3 characters long.

try:
    emp.salary = -1000  # Invalid salary
except ValueError as e:
    print(e)  # Output: Salary cannot be negative.

print("\n")



