# Create a dictionary to store key-value pairs.

# Creating a dictionary with key-value pairs
student_info = {
    "name": "John Doe",
    "age": 21,
    "major": "Computer Science",
    "GPA": 3.8
}

# Printing the dictionary
print("Student Information Dictionary:", student_info)

# Accessing a value using a key
print("Student's name:", student_info["name"])
print("Student's age:", student_info["age"])

# Adding a new key-value pair
student_info["graduation_year"] = 2025
print("Updated student information:", student_info)

# Modifying an existing value
student_info["GPA"] = 3.9
print("Updated GPA:", student_info["GPA"])

# Removing a key-value pair
del student_info["major"]
print("Updated student information after removing major:", student_info)
print("\n")


# Access, update, and delete dictionary elements using keys.

# Creating a sample dictionary
student_info = {
    "name": "Alice",
    "age": 22,
    "major": "Physics",
    "GPA": 3.7
}

# Accessing dictionary elements using keys
print("Accessing elements:")
print("Name:", student_info["name"])  # Accessing value for the key 'name'
print("Age:", student_info["age"])    # Accessing value for the key 'age'
print("Major:", student_info["major"])  # Accessing value for the key 'major'
print("GPA:", student_info["GPA"])    # Accessing value for the key 'GPA'

# Updating dictionary elements using keys
print("\nUpdating elements:")
student_info["age"] = 23  # Updating the value for key 'age'
student_info["GPA"] = 3.9  # Updating the value for key 'GPA'
print("Updated Age:", student_info["age"])
print("Updated GPA:", student_info["GPA"])

# Deleting dictionary elements using keys
print("\nDeleting elements:")
del student_info["major"]  # Deleting the key 'major'
print("Dictionary after deleting 'major':", student_info)

# Attempting to access a deleted key (will raise KeyError)
try:
    print("Major:", student_info["major"])
except KeyError:
    print("The key 'major' does not exist anymore.")
print("\n")


# Use dictionary methods like keys(), values(), and items()

# Creating a sample dictionary
student_info = {
    "name": "Bob",
    "age": 25,
    "major": "Mathematics",
    "GPA": 3.8
}

# Using keys() to get all the keys in the dictionary
print("Keys in the dictionary:", student_info.keys())

# Using values() to get all the values in the dictionary
print("Values in the dictionary:", student_info.values())

# Using items() to get all the key-value pairs as tuples
print("Key-Value pairs in the dictionary:", student_info.items())

# Iterating over keys, values, and items
print("\nIterating through the keys:")
for key in student_info.keys():
    print(key)

print("\nIterating through the values:")
for value in student_info.values():
    print(value)

print("\nIterating through the key-value pairs:")
for key, value in student_info.items():
    print(f"{key}: {value}")
print("\n")


# Add a new key-value pair and remove an existing key-value pair.

# Creating a sample dictionary
student_info = {
    "name": "Sarah",
    "age": 22,
    "major": "Engineering",
    "GPA": 3.7
}

# Adding a new key-value pair
student_info["graduation_year"] = 2024
print("Dictionary after adding a new key-value pair:", student_info)

# Removing an existing key-value pair
del student_info["major"]  # Removes the key 'major' and its associated value
print("Dictionary after removing the 'major' key:", student_info)

# Alternatively, using pop() to remove a key-value pair
removed_value = student_info.pop("GPA")  # Removes the 'GPA' key and returns its value
print("Removed GPA:", removed_value)
print("Dictionary after removing the 'GPA' key using pop:", student_info)
print("\n")


# Create a nested dictionary to store student details (like name, age, and marks)

# Creating a nested dictionary to store student details
students_info = {
    "student1": {
        "name": "Alice",
        "age": 20,
        "marks": {
            "math": 85,
            "science": 90,
            "english": 88
        }
    },
    "student2": {
        "name": "Bob",
        "age": 22,
        "marks": {
            "math": 78,
            "science": 85,
            "english": 80
        }
    },
    "student3": {
        "name": "Charlie",
        "age": 21,
        "marks": {
            "math": 92,
            "science": 89,
            "english": 91
        }
    }
}

# Printing the entire nested dictionary
print("Student Details:", students_info)

# Accessing specific details using keys
print("\nDetails of student1:")
print("Name:", students_info["student1"]["name"])
print("Age:", students_info["student1"]["age"])
print("Math Marks:", students_info["student1"]["marks"]["math"])

print("\nDetails of student2:")
print("Name:", students_info["student2"]["name"])
print("Age:", students_info["student2"]["age"])
print("Science Marks:", students_info["student2"]["marks"]["science"])

print("\nDetails of student3:")
print("Name:", students_info["student3"]["name"])
print("Age:", students_info["student3"]["age"])
print("English Marks:", students_info["student3"]["marks"]["english"])
print("\n")


# Access and update elements in a nested dictionary

# Creating a nested dictionary to store student details
students_info = {
    "student1": {
        "name": "Alice",
        "age": 20,
        "marks": {
            "math": 85,
            "science": 90,
            "english": 88
        }
    },
    "student2": {
        "name": "Bob",
        "age": 22,
        "marks": {
            "math": 78,
            "science": 85,
            "english": 80
        }
    },
    "student3": {
        "name": "Charlie",
        "age": 21,
        "marks": {
            "math": 92,
            "science": 89,
            "english": 91
        }
    }
}

# Accessing elements in the nested dictionary
print("Accessing elements:")
print("Student1's Name:", students_info["student1"]["name"])
print("Student2's Math Marks:", students_info["student2"]["marks"]["math"])

# Updating elements in the nested dictionary
# Updating Bob's science marks
students_info["student2"]["marks"]["science"] = 90
print("\nUpdated Science Marks for Bob:", students_info["student2"]["marks"]["science"])

# Updating Alice's age
students_info["student1"]["age"] = 21
print("\nUpdated Age for Alice:", students_info["student1"]["age"])

# Adding a new key-value pair for student3 (new subject marks)
students_info["student3"]["marks"]["history"] = 85
print("\nAdded History Marks for Charlie:", students_info["student3"]["marks"]["history"])

# Printing the updated nested dictionary
print("\nUpdated Nested Dictionary:")
print(students_info)
print("\n")

# Merge two dictionaries using update().

# Creating two sample dictionaries
dict1 = {
    "name": "Alice",
    "age": 25,
    "city": "New York"
}

dict2 = {
    "major": "Computer Science",
    "GPA": 3.9
}

# Merging dict2 into dict1 using the update() method
dict1.update(dict2)

# Printing the merged dictionary
print("Merged Dictionary:", dict1)
print("\n")


# Sample dictionary
my_dict = {'apple': 10, 'banana': 5, 'cherry': 7, 'date': 3}

# Sorting the dictionary based on values
sorted_dict = dict(sorted(my_dict.items(), key=lambda item: item[1]))

# Printing the sorted dictionary
print("Sorted dictionary by values:",sorted_dict)