# np.array(): Create a NumPy array from a list or tuple.

import numpy as np
list_data = [1, 2, 3, 4, 5]
array_from_list = np.array(list_data)
print(array_from_list)
print("\n")



# 2. np.zeros(): Create an array filled with zeros.
zeros_array = np.zeros((3, 3))
print(zeros_array)
print("\n")



# 3. np.ones(): Create an array filled with ones.
ones_array = np.ones((2, 2))  
print(ones_array)
print("\n")



# 4. np.arange(): Create an array with a range of values.
range_array = np.arange(0, 10, 2)  
print(range_array)
print("\n")



# 5. np.linspace(): Create an array with evenly spaced values over a specified interval.
linspace_array = np.linspace(0, 1,5)  
print(linspace_array)
print("\n")



# 6. np.reshape(): Change the shape of an array without changing its data.
import numpy as np

# Define the array with 5 elements
range_array = np.array([0, 2, 4, 6, 8])

# Reshape the array to (5, 1) since it has 5 elements
reshaped_array = range_array.reshape(5, 1)
print(reshaped_array)
print("\n")



# 7. np.flatten(): Convert a multi-dimensional array into a 1D array.
flattened_array = reshaped_array.flatten()  
print(flattened_array)
print("\n")



# 8. np.transpose(): Transpose an array (swap rows and columns).
transposed_array = reshaped_array.T  
print(transposed_array)
print("\n")



# 9. np.concatenate(): Join two or more arrays along an axis.
array1 = np.array([1, 2, 3])
array2 = np.array([4, 5, 6])
concatenated_array = np.concatenate((array1, array2))  
print(concatenated_array)
print("\n")



# 10. np.split(): Split an array into multiple sub-arrays.
split_array = np.split(concatenated_array, 2)  
print(split_array)
print("\n")



# 11. np.vstack(): Stack arrays vertically (row-wise).
vstack_array = np.vstack((array1, array2)) 
print(vstack_array)
print("\n")



# 12. np.hstack(): Stack arrays horizontally (column-wise).
hstack_array = np.hstack((array1, array2))  
print(hstack_array)
print("\n")



# 13. np.append(): Append values to the end of an array.
appended_array = np.append(array1, 7)
print(appended_array)
print("\n")



# 14. np.delete(): Delete elements from an array along a specified axis.
deleted_array = np.delete(array1, 1)  
print(deleted_array)
print("\n")



# 15. np.insert(): Insert values into an array at specified positions.
inserted_array = np.insert(array1, 1, 99) 
print(inserted_array)
print("\n")



# 16. arr[i]: Access an element of an array at index i.
accessed_element = inserted_array[2] 
print(accessed_element)
print("\n")



# 17. arr[i:j]: Slice an array from index i to j (exclusive).
sliced_array = array1[1:3]  
print(sliced_array)
print("\n")



# 18. arr[start:end:step]: Slice an array with a step between start and end.
stepped_slice = array1[::2] 
print(stepped_slice)
print("\n")



# 19. arr[:, :]: Access all elements along rows and columns (for 1D, 2D, and 3D arrays).
multi_dim_array = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
accessed_all = multi_dim_array[:, :] 
print(accessed_all)
print("\n")