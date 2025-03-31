#Write a program to count the frequency of each word in a string and store it in a dictionary.

input_str="Hello world Hello again, world"
words=input_str.split()
count={}

for word in words:
    word=word.lower()
    if word in count:
        count[word]+=1
    else:
        count[word]=1
print(count)
print("\n")


#Implement a simple phonebook application using a dictionary where users can add, delete, and search for contacts.

phonebook = {}
while True:
    print("\nPhonebook Menu:")
    print("1.Add a contact")
    print("2.Delete a contact")
    print("3.Search for a contact")
    print("4.Exit")
    ch=input("Enter your choice:")
    if ch=='1':
        name=input("Enter the contact name:")
        number=input("Enter the phone number:")
        phonebook[name]=number
        print(f"Contact {name} added successfully!")
    elif ch=='2':
        name=input("Enter the contact name to delete: ")
        if name in phonebook:
            del phonebook[name]
            print(f"Contact {name} deleted successfully!")
        else:
            print("Contact not found!")
    elif ch=='3':
        name=input("Enter the contact name to search: ")
        if name in phonebook:
            print(f"{name}'s phone number is {phonebook[name]}")
        else:
            print("Contact not found!")
    elif ch=='4':
        print("Exiting phonebook...")
        break
    else:
        print("Invalid choice, please try again.")
print("\n")


#Create a dictionary of students and their grades. Write a program to filter students who scored more than a specific mark.

students_grades={
    "Aarav": 85,
    "Mohan": 92,
    "Ishaan": 78,
    "Mann": 88,
    "Arjun": 95,
    "Sam": 70
}

threshold=int(input("Enter the threshold mark: "))
students={name: grade for name, grade in students_grades.items() if grade>threshold}

if students:
    print("\nStudents who scored more than", threshold, "are:")
    for name, grade in students.items():
        print(f"{name}: {grade}")
else:
    print(f"\nNo students scored more than {threshold}.")
print("\n")


#Write a program to convert a list of tuples (key-value pairs) into a dictionary and vice versa.

tuple_list=[("Sam",85),("Mohan",92),("Aarav",78),("Mann",88)]

converted_dict=dict(tuple_list)
print("Converted dictionary from tuple list:", converted_dict)

dict_to_tuple_list=list(converted_dict.items())
print("Converted list of tuples from dictionary:", dict_to_tuple_list)
print("\n")


