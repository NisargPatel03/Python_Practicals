# Write a code to open a file in read, write, or append mode using the open function using python. 

def file_operations(filename, mode, content=None):
    try:
        if mode == 'r':
            with open(filename, 'r') as file:
                data = file.read()
                print("File content:\n", data)
        
        elif mode == 'w':
            with open(filename, 'w') as file:
                file.write(content if content else "")
                print(f"Content written to {filename}")
        
        elif mode == 'a':
            with open(filename, 'a') as file:
                file.write(content if content else "")
                print(f"Content appended to {filename}")
        
        else:
            print("Invalid mode! Use 'r' for read, 'w' for write, or 'a' for append.")
    
    except FileNotFoundError:
        print("Error: The file does not exist. Please check the filename.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Example Usage
filename = "example.txt"

# Writing to a file
file_operations(filename, 'w',"This is the first line.\n")

# Appending to a file
file_operations(filename, 'a', "This is an appended line.\n")

# Reading the file
file_operations(filename, 'r')

print("\n")



# Write a program to read the entire content of a file using read(), readline(), readlines().

def read_file_using_methods(filename):
   
    try:
        # Using read()
        print("Reading entire content using read():")
        with open(filename, 'r') as file:
            content = file.read()
            print(content)
        print("-" * 50)

        # Using readline()
        print("Reading line by line using readline():")
        with open(filename, 'r') as file:
            line = file.readline()
            while line:
                print(line.strip())  # Strip removes extra newline characters
                line = file.readline()
        print("-" * 50)

        # Using readlines()
        print("Reading all lines into a list using readlines():")
        with open(filename, 'r') as file:
            lines = file.readlines()
            for line in lines:
                print(line.strip())  # Strip removes extra newline characters
        print("-" * 50)

    except FileNotFoundError:
        print(f"Error: The file '{filename}' does not exist.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage
filename = "sample.txt"

# Creating a sample file for demonstration
with open(filename, 'w') as f:
    f.write("First line\nSecond line\nThird line\n")

# Calling the function to read the file
read_file_using_methods(filename)

print("\n")



# Write a program to write data to a file using write() and writelines()

def write_to_file(filename):
    try:
        # Using write()
        with open(filename, 'w') as file:
            file.write("This is the first line.\n")
            file.write("This is the second line.\n")
        print("Data written to file using write().")

        # Using writelines()
        lines = ["This is the third line.\n", "This is the fourth line.\n"]
        with open(filename, 'a') as file:  # 'a' mode to append content
            file.writelines(lines)
        print("Data written to file using writelines().")

    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage
filename = "output.txt"
write_to_file(filename)

# Reading the file to verify content
print("\nVerifying written content:")
with open(filename, 'r') as file:
    print(file.read())

print("\n")



# Write a program to append data to the end of a file using write() in append mode.

def append_to_file(filename, data):

    try:
        with open(filename, 'a') as file:
            file.write(data + "\n")  # Appending data with a newline
        print("Data appended to the file successfully.")

    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage
filename = "append_example.txt"

# Creating the file with initial content (if not already present)
with open(filename, 'w') as file:
    file.write("Initial content in the file.\n")

# Appending data
append_to_file(filename, "This is the first appended line.")
append_to_file(filename, "This is the second appended line.")

# Verifying the content of the file
print("\nVerifying appended content:")
with open(filename, 'r') as file:
    print(file.read())

print("\n")



