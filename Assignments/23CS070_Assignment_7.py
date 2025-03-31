# 1. Create a new file, write content, close it, then reopen and read content
with open("newfile.txt", "w") as file:
    file.write("Hello, this is a sample file for Assignment 7.\nPython file handling is interesting!")

with open("newfile.txt", "r") as file:
    content = file.read()

print("\nFile Content:\n", content)

# 2. Read a list of numbers and separate odd/even numbers into respective files
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

with open("odd_numbers.txt", "w") as odd_file, open("even_numbers.txt", "w") as even_file:
    for num in numbers:
        (odd_file if num % 2 else even_file).write(f"{num}\n")

print("\nOdd and even numbers have been saved to respective files.")

# 3. Read a text file and print any 5 words from it
with open("sample_text.txt", "w") as file:
    file.write("Python makes file handling easy and efficient. We can read, write, and manipulate files.")

with open("sample_text.txt", "r") as file:
    words = file.read().split()

print("\nFive words from the file:", " ".join(words[:5]))

# 4. Generate a triangle pattern of 5 rows and save it to a file
triangle_pattern = "\n".join("*" * (i + 1) for i in range(5))

with open("triangle.txt", "w") as file:
    file.write(triangle_pattern)

print("\nTriangle pattern saved to triangle.txt.")
