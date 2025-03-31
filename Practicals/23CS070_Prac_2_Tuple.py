# Create tuples with different data types (integer, float, string, and mixed). 
int_tupple = (1, 2, 3, 4, 5)
print("Int Tupple: ",int_tupple)

float_tupple = (1.1, 2.2, 3.3, 4.4, 5.5)
print("Float Tupple: ",float_tupple)

string_tupple = ("Nisarg", "Patel")
print("String Tupple: ",string_tupple)

mixed_tupple = (1, 2.2, "Hello")
print("Mixed Tupple: ",mixed_tupple)
print("\n")

# Access tuple elements using positive and negative indices. 
print("Element at index-0(positive index): ",int_tupple[0])
print("Element at index-4(positive index): ",int_tupple[4])
print("Element at index-(-2)(negative index): ",int_tupple[-2])
print("Element at index-(-3)(negative index): ",int_tupple[-3])
print("\n")

# Perform tuple slicing to extract specific portions of the tuple. 
sample_tupple = (10, 20, 30, 40, 50, 60, 70, 80, 90, 100)

slice_1 = sample_tupple[2:6]
print("Elements from index-2 to index-5: ",slice_1)

slice_2 = sample_tupple[:5]
print("Elements from the beginning up to index-4: ",slice_2)

slice_3 = sample_tupple[3:]
print("Elements from index-3 to end: ",slice_3)

slice_4 = sample_tupple[::2]
print("Elements with a step of 2: ",slice_4)

slice_5 = sample_tupple[-3:]
print("Last 3 Elements: ",slice_5)

slice_6 = sample_tupple[::-1]
print("Tupple in Reverse Order: ",slice_6)
print("\n")

# Count occurrences of an element and find the index of an element in a tuple. 
sample = (10, 20, 30, 40, 30, 50, 30, 60)

occurrences = sample.count(30)
print("Occurrences of 30: ",occurrences)

index_of_20 = sample.index(20)
print("Index of 20 is: ",index_of_20)

try:
    index_of_100 = sample.index(100)
    print("Index of 100 is: ",index_of_100)
except ValueError:
    print("100 is not in the tupple")
print("\n")

# Use built-in functions like len(), max(), min(), and sum() with tuples. 
sample_tuple = (1, 2, 3, 4, 5)

length = len(sample_tuple)
print("Length of Tupple is: ",length)

max_value = max(sample_tuple)
print("Maximum of Tupple is: ",max_value)

min_value = min(sample_tuple)
print("Minimum of Tupple is: ",min_value)

total_sum = sum(sample_tuple)
print("Total sum: ", total_sum)
print("\n")
    
# Write a program to count and print distinct elements from a tuple. 
sample_tupple = (10, 20, 20, 30, 10, 40, 50, 30, 30)

distinct_element = set(sample_tupple)
print("Distinct Element: ",distinct_element)

for element in distinct_element:
    count = sample_tupple.count(element)
    print(f"Element {element} occurs {count} time(s).")
