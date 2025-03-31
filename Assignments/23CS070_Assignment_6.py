# main.py
from math_utils import basic_arithmetic, is_even_or_odd
from geometry_number import calculate_area, is_prime
from datetime import datetime

# Using math_utils module
print("Math Utils Module Demo:")
print(f"5 + 3 = {basic_arithmetic(5, 3, 'add')}")
print(f"10 - 4 = {basic_arithmetic(10, 4, 'subtract')}")
print(f"6 * 2 = {basic_arithmetic(6, 2, 'multiply')}")
print(f"15 / 3 = {basic_arithmetic(15, 3, 'divide')}")
print(f"Is 7 even or odd? {is_even_or_odd(7)}")
print(f"Is 8 even or odd? {is_even_or_odd(8)}")

print("\nGeometry and Number Module Demo:")
# Using geometry_number module
print(f"Area of circle (r=5): {calculate_area('circle', radius=5):.2f}")
print(f"Area of rectangle (l=4, w=6): {calculate_area('rectangle', length=4, width=6)}")
print(f"Area of triangle (b=3, h=8): {calculate_area('triangle', base=3, height=8)}")
print(f"Is 17 prime? {is_prime(17)}")
print(f"Is 24 prime? {is_prime(24)}")

# Using datetime module
print("\nDateTime Demo:")
current = datetime.now()
print(f"Current date and time: {current}")
print(f"Formatted date: {current.strftime('%B %d, %Y %I:%M %p')}")
print(f"Short format: {current.strftime('%m/%d/%Y %H:%M')}")