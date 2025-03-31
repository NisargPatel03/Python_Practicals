#Write a program to remove duplicate elements from a list using a set.

my_list=[1,2,2,3,4,4,5,6,6,7]
set_list=list(set(my_list))
print("After removing duplicates from the list:", set_list)
print("\n")


#Write a program to find the symmetric difference of multiple sets

set1={1, 2, 3, 4}
set2={3, 4, 5, 6}
set3={5, 6, 7, 8}

result=set1^set2^set3
print("Symmetric difference:", result)
print("\n")


#Write a program to find the intersection of two sets where one set has even numbers and another has prime numbers.

even={2,4,6,8,10}
prime={2,3,5,7}

intersection=even&prime
print("Intersection of even and prime numbers:", intersection)
print("\n")


#Write a program to find the union of two sets where one set has odd numbers and another has multiple of 9’s.

odd={1,3,5,7,9}
multiples_of_nine={9,18,27,36,45}

union=odd|multiples_of_nine
print("Union of odd numbers and multiples of 9:",union)
print("\n")


#Write a program to find the difference of two sets where one set has positive numbers and another has negative numbers

p_nums={1,2,3,4,5}
n_nums={-1,-2,-3,-4,-5}

diff_set=p_nums-n_nums
print("Difference of positive and negative number sets:", diff_set)
print("\n")