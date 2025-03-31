import math
import datetime
import sys
import importlib

# Task 1: Import a module and use a function
print("Square root of 25:", math.sqrt(25))

# Task 2: Use a module to work with dates and times
current_time = datetime.datetime.now()
print("Current date and time:", current_time)

# Task 3: Create and use a custom module (importing custom_module.py)
import custom_module  # Assume this file contains a function custom_function()
custom_module.custom_function()

# Task 4: Work with a package in Python (Assuming a package 'mypackage' exists)
from mypackage import submodule
submodule.sub_function()

# Task 5: Check if a package is installed
try:
    import numpy
    print("NumPy is installed.")
except ImportError:
    print("NumPy is not installed.")

# Task 6: Use pip to install a third-party package (run in terminal)
# pip install requests

# Task 7: Use sys module to manipulate the module search path
sys.path.append('/path/to/custom/modules')  # Modify as needed
print("Updated sys.path:", sys.path)

# Task 8: Reload a module after making changes
importlib.reload(custom_module)

# Task 9: Create a package with an __init__.py file and use its submodules (Handled in mypackage)

# Task 10: Check the version of an installed package
import subprocess
subprocess.run(["pip", "show", "numpy"])

# Task 11: List all installed packages
subprocess.run(["pip", "list"])

# Task 12: Uninstall a package using pip (run in terminal)
# pip uninstall numpy
