#Create a student class with attributes for name, age, and grades, and methods to calculate the average grade and display student information.

class Student:
    def __init__(self, name, age, grades):
        self.name = name
        self.age = age
        self.grades = grades

    def average_grade(self):
        return sum(self.grades) / len(self.grades) if self.grades else 0

    def display_info(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Average Grade: {self.average_grade():.2f}")

# Getting user input
name = input("Enter student name: ")
age = int(input("Enter student age: "))
grades = list(map(int, input("Enter grades separated by spaces: ").split()))

student1 = Student(name, age, grades)
student1.display_info()
print("\n")



# Create a BankAccount class with attributes for account number, balance, and account type, and methods to deposit, withdraw, and display account information.
class BankAccount:
    def __init__(self, account_number, balance, account_type):
        self.account_number = account_number
        self.balance = balance
        self.account_type = account_type

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited: {amount}. New Balance: {self.balance}")
        else:
            print("Invalid deposit amount.")

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f"Withdrawn: {amount}. New Balance: {self.balance}")
        else:
            print("Invalid withdrawal amount or insufficient balance.")

    def display_info(self):
        print(f"Account Number: {self.account_number}")
        print(f"Account Type: {self.account_type}")
        print(f"Balance: {self.balance:.2f}")

# Example usage with switch-case like structure
def main():
    account1 = BankAccount("12345678", 1000.0, "Savings")
    while True:
        print("\n1. Display Account Info")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Exit")
        choice = input("Enter your choice: ")
        match choice:
            case "1":
                account1.display_info()
            case "2":
                amount = float(input("Enter amount to deposit: "))
                account1.deposit(amount)
            case "3":
                amount = float(input("Enter amount to withdraw: "))
                account1.withdraw(amount)
            case "4":
                print("Exiting...")
                break
            case _:
                print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()

print("\n")



#Create a Person superclass with attributes for name and age, and a Student subclass that inherits from Person and adds an attribute for student ID and a method to display student information.

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def display_info(self):
        print(f"Name: {self.name}, Age: {self.age}")

class Student(Person):
    def __init__(self, name, age, student_id):
        super().__init__(name, age)
        self.student_id = student_id
    
    def display_student_info(self):
        print(f"Name: {self.name}, Age: {self.age}, Student ID: {self.student_id}")

# Example usage:
name = input("Enter name: ")
age = int(input("Enter age: "))
student_id = input("Enter student ID: ")

student = Student(name, age, student_id)
student.display_student_info()