"""Conditional statements allow your program to make decisions.
In simple words:
If something is true, do this; otherwise, do something else."""

age = 20
if age >= 18:
    print("You are an adult")

# Without conditions, a program would always execute the same instructions.
"""
Login
 ↓
Is username/password correct?
 ├── Yes → Login successful
 └── No  → Login failed
 """


# if Statement

# if condition:
#     code

# Python uses indentation to define blocks (use 4 spaces)

age = 20
if age >= 18:
    print("Adult")

#           age >= 18
#               │
#          ┌────┴────┐
#        True       False
#          │
#          ▼
#    print("Adult")

# Multiple Statements Inside if
age = 20
if age >= 18:
    print("You are an adult")
    print("You can vote")
    print("You can apply for a driving license")

# else - if the condition is false
age = 15
if age >= 18:
    print("Adult")
else:
    print("Minor")

# if + else Flow

#                  condition
#                      │
#              ┌───────┴───────┐
#            True             False
#              │                 │
#              ▼                 ▼
#        if block           else block

# elif - more than two possibilities
marks = 75
if marks >= 90:
    print("A+")
elif marks >= 80:
    print("A")
elif marks >= 70:
    print("B")
elif marks >= 60:
    print("C")
else:
    print("D")

#  Multiple Conditions with and  - all conditions must be true
age = 25
has_id = True
if age >= 18 and has_id:
    print("Access granted")
else:
    print("Access denied")

# Multiple Conditions with or - at least one condition must be true
is_admin = False
is_manager = True
if is_admin or is_manager:
    print("Access granted")

# not reverses a Boolean condition
is_logged_in = False
if not is_logged_in:
    print("Please login")

# Combining and, or, not
age = 25
is_member = True
is_blocked = False
if age >= 18 and is_member and not is_blocked:
    print("Access granted")

# Use Parentheses for Complex Conditions
if (age >= 18 and is_member) or is_admin:
    print("Welcome")

# if statement can exist inside another if
age = 25
has_id = True
if age >= 18:
    if has_id:
        print("Access granted")
    else:
        print("ID required")
else:
    print("Underage")


# Nested if vs and
if age >= 18:
    if has_id:
        print("Access granted")

# User Input + elif
marks = int(input("Enter your marks: "))
if marks >= 90:
    print("Grade A+")
elif marks >= 80:
    print("Grade A")
elif marks >= 70:
    print("Grade B")
elif marks >= 60:
    print("Grade C")
else:
    print("Grade D")


# Membership Conditions
skills = ["Python", "JavaScript", "React"]
if "Python" in skills:
    print("Python is available")


# match / case - matching a value against multiple possible patterns
command = "start"
match command:
    case "start":
        print("Starting...")
    case "stop":
        print("Stopping...")
    case "restart":
        print("Restarting...")
    case _:
        print("Unknown command")


# match with Multiple Values
day = "Saturday"
match day:
    case "Saturday" | "Sunday":
        print("Weekend")
    case "Monday" | "Tuesday" | "Wednesday" | "Thursday" | "Friday":
        print("Weekday")
    case _:
        print("Invalid day")

# match with Conditions — Guards
age = 25
match age:
    case age if age < 18:
        print("Minor")
    case age if age >= 18:
        print("Adult")


# match with Data Structures
response = {
    "status": 200,
    "message": "Success",
}

match response:
    case {"status": 200}:
        print("Request successful")
    case {"status": 404}:
        print("Not found")
    case {"status": 500}:
        print("Server error")
    case _:
        print("Unknown response")

# Advanced: Pattern Matching
user = {
    "role": "admin",
    "active": True,
}
match user:
    case {"role": "admin", "active": True}:
        print("Active admin")
    case {"role": "admin"}:
        print("Admin")
    case _:
        print("Other user")


# Advanced: Matching and Extracting Values
user = {
    "name": "Vikrant",
    "age": 39,
}

match user:
    case {"name": name, "age": age}:
        print(f"{name} is {age} years old")
    case _:
        print("Invalid user")

# Conditional Logic Inside Loops
numbers = [1, 2, 3, 4, 5]
for number in numbers:
    if number % 2 == 0:
        print(number, "is even")
    else:
        print(number, "is odd")

# continue with Conditions
for number in numbers:
    if number % 2 != 0:
        continue

    print(number)

# break with Conditions
for number in numbers:
    if number == 3:
        break

    print(number)

#API Example
response = {
    "status": 200,
    "data": ["Ankit", "Manish"],
}
if response["status"] == 200:
    print("Request successful")
elif response["status"] == 404:
    print("Data not found")
elif response["status"] == 500:
    print("Server error")
else:
    print("Unknown response")
    
# Beginner to Advanced
# 1. True / False
#        ↓
# 2. Comparison operators
#        ↓
# 3. if
#        ↓
# 4. if + else
#        ↓
# 5. if + elif + else
#        ↓
# 6. Logical operators
#        ↓
# 7. Nested if
#        ↓
# 8. Truthy / Falsy
#        ↓
# 9. in / not in
#        ↓
# 10. is / is not
#        ↓
# 11. Conditional expressions
#        ↓
# 12. Conditions + loops
#        ↓
# 13. Guard clauses
#        ↓
# 14. Complex business conditions
#        ↓
# 15. match / case
#        ↓
# 16. Structural pattern matching

