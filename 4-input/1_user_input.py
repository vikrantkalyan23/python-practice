# User input means taking information from the user while the Python program is running

# Input Functions and Methods

# input()
#   ↓
# strip()
#   ↓
# lower() / upper()
#   ↓
# split()
#   ↓
# int() / float()
#   ↓
# try / except

# input() - (Always Returns a String)
name = input("Enter your name: ")
print("Name : ", name)

age = input("Enter your age: ")
print("Age : ", age)
print(type(age))

# Why Does This Matter? Suppose you want to add two numbers:
num1 = input("Enter first number: ")
num2 = input("Enter second number: ")
result = num1 + num2
print("Total : ", result)

# int() - Convert Input to Integer
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
result = num1 + num2
print("Total : ", result)
print(type(num1))

# float() - Float Input
price = float(input("Enter price: "))
print(price)
print(type(price))

# Boolean Input (careful with Boolean input)
answer = input("Are you admin? ").strip().lower()
is_admin = answer == "yes"
print(is_admin)

# strip() removes unnecessary spaces from the beginning and end of the input.
name = input("Enter your name: ").strip()
print(name)

# lower() and upper()
choice = input("Enter yes or no: ").strip().lower()
print(choice)

choice = input("Continue? ").strip().lower()
if choice == "yes":
    print("Continuing...")
else:
    print("Stopping...")


name = input("Enter your name: ")
print(name.upper())

# Multiple Values From One Input
values = input("Enter two numbers: ").split()
print(values)

# multiple numbers
num1, num2 = map(int, input("Enter two numbers: ").split())
print(num1 + num2)

# Taking Multiple Strings
first_name, last_name = input("Enter your full name: ").split()
print(first_name)
print(last_name)

# Input as a List of Numbers
numbers = list(map(int, input("Enter numbers: ").split()))
print(numbers)

# Input as a List of Strings
skills = input("Enter your skills: ").split()
print(skills)

# Input With a Comma
skills = input("Enter skills: ").split(",")
print(skills)

# You can clean spaces too:
skills = [skill.strip() for skill in input("Enter skills: ").split(",")]
print(skills)

# User Input With Multiple Conditions
age = int(input("Enter your age: "))
has_id = input("Do you have an ID? ").strip().lower()
if age >= 18 and has_id == "yes":
    print("Access granted")
else:
    print("Access denied")

# Handling Invalid Input Using try/except
try:
    age = int(input("Enter your age: "))
    print("Your age is:", age)
except ValueError:
    print("Please enter a valid number.")

# Input Validation With a Loop
while True:
    try:
        age = int(input("Enter your age: "))
        break
    except ValueError:
        print("Please enter a valid number.")
print("Your age is:", age)


# Example
name = input("Enter employee name: ").strip()
age = int(input("Enter employee age: "))
salary = float(input("Enter employee salary: "))

print(f"""
Employee Details
----------------
Name: {name}
Age: {age}
Salary: ₹{salary:.2f}
""")
