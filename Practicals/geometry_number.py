# geometry_number.py
import math

def calculate_area(shape, **kwargs):
    """Calculate area of different shapes"""
    if shape == 'circle':
        radius = kwargs.get('radius', 0)
        return math.pi * radius * radius
    elif shape == 'rectangle':
        length = kwargs.get('length', 0)
        width = kwargs.get('width', 0)
        return length * width
    elif shape == 'triangle':
        base = kwargs.get('base', 0)
        height = kwargs.get('height', 0)
        return 0.5 * base * height
    else:
        return "Invalid shape"

def is_prime(number):
    """Check if a number is prime"""
    if number < 2:
        return False
    for i in range(2, int(math.sqrt(number)) + 1):
        if number % i == 0:
            return False
    return True