# Create a set to store unique elements.

# Create an empty set
unique_elements = set()

# Add elements to the set
unique_elements.add(1)
unique_elements.add(2)
unique_elements.add(3)
unique_elements.add(1)  # This will not be added again as sets only store unique elements

# Print the set
print("Set of unique elements:", unique_elements)
print("\n")


# Add elements to a set.

# Create a set
my_set = {1, 2, 3}

# Add a single element
my_set.add(4)

# Print the updated set
print("Set after adding a single element:", my_set)


# Add a multiple element

# Create a set
my_set = {1, 2, 3}

# Add multiple elements using the update() method
my_set.update([4, 5, 6])

# Print the updated set
print("Set after adding multiple elements:", my_set)
print("\n")


# Remove elements from a set

# Create a set
my_set = {1, 2, 3, 4, 5}

# Remove an element
my_set.remove(3)

# Print the updated set
print("Set after removing an element:", my_set)



# Create a set
my_set = {1, 2, 3, 4, 5}

# Discard an element
my_set.discard(3)

# Print the updated set
print("Set after discarding an element:", my_set)

# Discarding an element that doesn't exist will not raise an error
my_set.discard(10)  # No error even though 10 isn't in the set
print("Set after discarding a non-existing element:", my_set)



# Create a set
my_set = {1, 2, 3, 4, 5}

# Pop an arbitrary element
popped_element = my_set.pop()

# Print the popped element and the updated set
print("Popped element:", popped_element)
print("Set after popping an element:", my_set)



# Create a set
my_set = {1, 2, 3, 4, 5}

# Clear all elements from the set
my_set.clear()

# Print the cleared set
print("Set after clearing all elements:", my_set)
print("\n")


# Combine elements from two sets.


# Define two sets
set1 = {1, 2, 3}
set2 = {3, 4, 5}

# Combine the sets using union() method
combined_set = set1.union(set2)

# Print the combined set
print("Combined set using union():", combined_set)



# Define two sets
set1 = {1, 2, 3}
set2 = {3, 4, 5}

# Combine the sets using the | operator
combined_set = set1 | set2

# Print the combined set
print("Combined set using | operator:", combined_set)
print("\n")


# Find common elements between two sets.

# Define two sets
set1 = {1, 2, 3, 4, 5}
set2 = {3, 4, 5, 6, 7}

# Find the common elements using intersection() method
common_elements = set1.intersection(set2)

# Print the common elements
print("Common elements using intersection():", common_elements)



# Define two sets
set1 = {1, 2, 3, 4, 5}
set2 = {3, 4, 5, 6, 7}

# Find the common elements using the & operator
common_elements = set1 & set2

# Print the common elements
print("Common elements using & operator:", common_elements)
print("\n")


# Find elements present in one set but not in another.

# Define two sets
set1 = {1, 2, 3, 4, 5}
set2 = {3, 4, 5, 6, 7}

# Find the elements in set1 but not in set2
difference_set = set1.difference(set2)

# Print the result
print("Elements in set1 but not in set2 using difference():", difference_set)



# Define two sets
set1 = {1, 2, 3, 4, 5}
set2 = {3, 4, 5, 6, 7}

# Find the elements in set1 but not in set2 using the - operator
difference_set = set1 - set2

# Print the result
print("Elements in set1 but not in set2 using - operator:", difference_set)
print("\n")


# Find elements present in either of the sets but not in their intersection.


# Define two sets
set1 = {1, 2, 3, 4, 5}
set2 = {3, 4, 5, 6, 7}

# Find the elements present in either of the sets but not in their intersection
symmetric_difference_set = set1.symmetric_difference(set2)

# Print the result
print("Elements in either of the sets but not in their intersection using symmetric_difference():", symmetric_difference_set)




# Define two sets
set1 = {1, 2, 3, 4, 5}
set2 = {3, 4, 5, 6, 7}

# Find the elements present in either of the sets but not in their intersection using ^ operator
symmetric_difference_set = set1 ^ set2

# Print the result
print("Elements in either of the sets but not in their intersection using ^ operator:", symmetric_difference_set)
print("\n")


# Check if one set is a subset of another.


# Define two sets
set1 = {1, 2, 3}
set2 = {1, 2, 3, 4, 5}

# Check if set1 is a subset of set2
is_subset = set1.issubset(set2)

# Print the result
print("Is set1 a subset of set2 using issubset():", is_subset)





# Define two sets
set1 = {1, 2, 3}
set2 = {1, 2, 3, 4, 5}

# Check if set1 is a subset of set2 using the <= operator
is_subset = set1 <= set2

# Print the result
print("Is set1 a subset of set2 using <= operator:", is_subset)
print("\n")


# Check if one set is a superset of another.


# Define two sets
set1 = {1, 2, 3, 4, 5}
set2 = {1, 2, 3}

# Check if set1 is a superset of set2
is_superset = set1.issuperset(set2)

# Print the result
print("Is set1 a superset of set2 using issuperset():", is_superset)




# Define two sets
set1 = {1, 2, 3, 4, 5}
set2 = {1, 2, 3}

# Check if set1 is a superset of set2 using the >= operator
is_superset = set1 >= set2

# Print the result
print("Is set1 a superset of set2 using >= operator:", is_superset)
print("\n")


# Remove all elements from a set.

# Define a set
my_set = {1, 2, 3, 4, 5}

# Remove all elements from the set
my_set.clear()

# Print the set after clearing
print("Set after removing all elements:", my_set)
