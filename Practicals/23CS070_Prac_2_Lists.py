# Create a list of integers, strings, and mixed data types.  
integer_list = [10, 20, 30, 40, 50]
print("List Of Integers: ",integer_list)

float_list = [10.10, 20.20, 30.30, 40.40, 50.50]
print("List Of Float: ",float_list)

string_list = ["Nisarg", "Patel"]
print("List of String: ",string_list)

mixed_list = [1, 2.2, "Hello"]
print("List of mixed: ",mixed_list)
print("\n")

# Access elements using indices, perform slicing, and update list elements. 
sample_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print("Element at index-2: ",sample_list[2])
print("Element at index-4: ",sample_list[4])
print("Element at index-(-1): ",sample_list[-1])
print("\n")

# Add and remove elements using append(), insert(), remove(), and pop() methods. 
sample_lists = [5, 10, 15, 20, 25]

sample_lists.append(30)
print("Lists after appending 30: ",sample_lists)

sample_lists.insert(1,35)
print("Lists after inserting 30 at index-1: ",sample_lists)

sample_lists.remove(20)
print("Lists after removing 20: ",sample_lists)

sample_lists.pop()
print("Lists after Pop operation: ", sample_lists)

sample_lists.pop(3)
print("Lists after popping at index-3: ",sample_lists)
print("\n")

# Concatenate and repeat lists using operators. 
list1 = [3, 6, 9]
list2 = [4, 8, 12]

concatenated_list = list1 + list2
print("Concatenated Lists: ",concatenated_list)

repeated_list = list1*4
print("Repeated Lists: ",repeated_list)
print("\n")

# Filter even numbers from a list using list comprehension. 
number_list = [5, 10, 15, 20, 25]

even_numbers = [x for x in number_list if x%2==0]

print("Even Numbers: ",even_numbers)
print("\n")

# Create a list of squares of the first 10 natural numbers using list comprehension.
numbers_list = [x**2 for x in range(1,11)]
print("Square of First 10 Natural Numbers: ",numbers_list)
print("\n")

# Demonstrate sorting, reversing, and copying lists. 
num_list = [5,4,2,7,8,0,6]
sorted_list = num_list.copy()
sorted_list.sort()

print("Sorted Lists: ",sorted_list)

reverse_list = num_list.copy()
reverse_list.reverse()
print("Reverse Lists: ",reverse_list)
print("\n")

# Write a program to remove duplicates from a list. 
sample_list = [10, 20, 30, 20, 40, 50, 30, 60, 10]

unique_list = list(set(sample_list))
print("List without Duplicate Elements: ",unique_list)
print("\n")