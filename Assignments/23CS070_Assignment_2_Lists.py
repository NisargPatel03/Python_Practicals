# Implement a program to generate a list of prime numbers within a given range. 
def isPrime(num):
    for i in range(2,num):
        if num%i==0:
            return None
    return True

def generate_primes(start,end):
    Prime_no = []
    for i in range(start,end):
        if isPrime(i):
            Prime_no.append(i)
    return Prime_no

print("Prime Numbers in the range of 2 to 70: ",generate_primes(2,70))
print("\n")


# Flatten a nested list using recursion. 
def flatten(nested_list):
    flat_list = []
    for item in nested_list:
        if isinstance(item,list):
            flat_list.extend(flatten(item))
        else:
            flat_list.append(item)
    return flat_list

nested_list = [1, [2,3], [4,5,6], [7,8,9,10]]
flatten_list = flatten(nested_list)

print("Flattened List: ",flatten_list)
print("\n")


# Write a program to find the second largest element from a list without using built-in functions. 
def second_largest(numbers):
    if len(numbers)<2:
        return None
    
    largest = second_largest = float('-inf')
    
    for num in numbers:
        if num>largest:
            second_largest = largest
            largest = num
        elif num>second_largest and num!=largest:
            second_largest=num
        
    if second_largest==float('-inf'):
            return None
        
    return second_largest

numbers = [1,5,9,69,7,75,70]
second_large = second_largest(numbers)
print("Second Largest Number is: ",second_large)
print("\n")


# Use a list to manage a task queue, where tasks are added, removed, and processed sequentially.
task_queue = []

def add_task(task):
    task_queue.append(task)
    print(f"Task '{task}' has been added to the queue")

def process_task():
    if task_queue:
        task = task_queue.pop(0)
        print(f"Processing Task: {task}")
    else:
        print("No Task in the queue to process")


add_task("Task-1")
add_task("Task-3")
add_task("Task-70")

process_task()
process_task()
process_task()
process_task()