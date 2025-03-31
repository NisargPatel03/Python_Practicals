# Write a function that takes a tuple as an argument and returns the tuple with all duplicates removed. 
def remove_duplicates(input_tuple):
    return tuple(set(input_tuple))
    
    
input_tuple = (1,2,3,4,5,6,2,5,6,1)
result_tuple = remove_duplicates(input_tuple)

print("Orignal Tuple: ",input_tuple)
print("Tuple after removing Duplicates: ",result_tuple)
print("\n")


# Create a list of tuples representing student names and marks, and sort the list by marks. 
Students = [(95,"Nisarg"), (92,"Tejas"), (85,"Megh")]
Students.sort()
print("After Sorting according to marks: ",Students)
print("\n")


# Write a program to count the frequency of elements in a tuple using Counter from the collections module. 
from collections import Counter

sample_tuple = (1,2,3,4,5,6,5,4,3,2,1,1)

element_count = Counter(sample_tuple)

print("Frequency of each Element is: ")
for element, count in element_count.items():
    print(f"Element: {element}, Frequency: {count}")
print("\n")

# Implement a tuple-based record system where each tuple represents a record (ID, Name, and Marks) and perform search operations. 
records = [(1, "Nisarg Patel", 70), (2, "Tejas Patel", 75), (3, "Megh Patel", 69), (4, "Prit Patel", 106), (5, "Aum Shah", 85)]

def search_by_ID(search_id):
        for record in records:
            if record[0] == search_id:
                return record
        return None
    
def search_by_marks(search_marks):
        for mark in records:
            if mark[2] == search_marks:
                return mark
        return None
    
def search_by_name(search_name):
        for name in records:
            if name[1].lower() == search_name.lower():
                return name
        return None
    
print("Searching for record with ID 3: ")
record = search_by_ID(3)
if record:
    print(f"Found Record: {record}")
else:
    print("Record Not Found.")
    
    
print("Searching for record with Name 'Nisarg Patel': ")
record = search_by_name("Nisarg Patel")
if record:
    print(f"Found Record: {record}")
else:
    print("Record Not Found.")
    
    
print("Searching for record with Marks 75: ")
record = search_by_marks(75)
if record:
    print(f"Found Record: {record}")
else:
    print("Record Not Found.")
