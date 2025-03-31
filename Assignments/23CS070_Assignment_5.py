# Create a Shape superclass with a method to calculate the area, and Circle and Rectangle subclasses that override the area calculation method to demonstrate polymorphism.

from math import pi

class Shape:
    def area(self):
        raise NotImplementedError("Subclass must implement abstract method")

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        return pi * self.radius ** 2

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def area(self):
        return self.width * self.height

def print_area(shape):
    print(f"The area is: {shape.area()}")

circle = Circle(5)
rectangle = Rectangle(4, 6)

print_area(circle)
print_area(rectangle)

print("\n")



# Create a Book class with private attributes for title, author, and ISBN, and public getter and setter methods to access and modify these attributes, demonstrating encapsulation.

class Book:
    def __init__(self, title, author, isbn):
        self.__title = title
        self.__author = author
        self.__isbn = isbn
    
    def get_title(self):
        return self.__title
    
    def get_author(self):
        return self.__author
    
    def get_isbn(self):
        return self.__isbn
    
    def set_title(self, title):
        self.__title = title
    
    def set_author(self, author):
        self.__author = author
    
    def set_isbn(self, isbn):
        self.__isbn = isbn

book = Book("1984", "George Orwell", "123-456-789")
print(f"Title: {book.get_title()}")
print(f"Author: {book.get_author()}")
print(f"ISBN: {book.get_isbn()}")

book.set_title("Animal Farm")
print(f"Updated Title: {book.get_title()}")

print("\n")