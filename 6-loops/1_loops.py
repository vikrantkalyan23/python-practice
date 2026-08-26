"""A loop allows you to execute the same block of code multiple times"""

for _ in range(5):
    print("Hello")

#     LOOP
#       │
#       ▼
# Execute code
#       │
#       ▼
# Check condition
#       │
#   ┌───┴───┐
#  Yes      No
#   │        │
#   └───►────┘
#       Stop

# Loops are useful whenever you need to perform an operation repeatedly
# Example 1 : Print numbers
for number in range(1, 6):
    print(number)

# Example 2 : Process employees
employees = ["Ankit", "Manish", "Neeraj"]
for employee in employees:
    print(employee)

# Example 3 : Keep asking for input
while True:
    value = input("Enter something (exit to break): ")
    if value == "exit":
        break

# loops are fundamental to:

# data processing
# API responses
# database records
# files
# user input
# automation
# algorithms
# machine learning
# web applications

# Types of Loops in Python

# Python Loops
# │
# ├── for loop
# │
# └── while loop

# Python also has some important loop-related concepts:

# for
# while
# break
# continue
# pass
# else with loops
# nested loops
# iterators
# iterables
# generators
