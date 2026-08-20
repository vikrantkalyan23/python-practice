"""A list allows to store multiple values in a single variable. Lists are Mutable, Mutable means you can change the list after creating it."""

""" Most Common List Operations
append()
extend()
insert()
remove()
pop()
clear()
index()
count()
sort()
reverse()
copy()
len()
min()
max()
sum()
sorted()
in
not in
"""

employees = ["Ankit", "Manish", "Sandeep"]
data = ["Ankit", 41, 5.8, True]  # Mixed data types
print("List of employees : ", employees)
print(data[0])  # indexing start from 0
print(data[3])

"""
              Positive
                 ↓
["Ankit", "Manish", "Neeraj"]
    0        1          2

   -3       -2         -1
                 ↑
              Negative
"""

print(data[-2])  # Negative indexing count from the end


# append() - adds an item to the end of the list.
employees.append("Neeraj")
print("List of employees : ", employees)

# extend() - adds multiple elements to the list.
employees.extend(["Uday", "Kapil"])
print("List of employees : ", employees)

# append() vs extend()
# employees.append(["Rahul","Rohit"]) # The entire list becomes one element
# print(employees)


# insert() — Add at a Specific Position
# syntax : list.insert(index, value)
employees.insert(1, "Yuvi")
print(employees)

# remove() — Remove by Value (removes the first matching value if multiple)
employees.remove("Manish")
print(employees)

# pop() — Remove by Index
# employee = employees.pop() # If you don't provide an index, it removes the last item.
employee = employees.pop(1)
print(employee)
print(employees)

# clear() — Remove Everything (The list still exists, but it is empty.)
employees1 = ["Ankit", "Manish", "Neeraj"]
employees1.clear()
print("After Clear : ", employees1)

# len() — Get Number of Items
print("Length of employees list : ", len(employees))

# Very common:
if len(employees) > 0:
    print("Employees exist")
# But Python provides a cleaner way:
if employees:
    print("Employees exist")

# in — Check Whether an Item Exists
print("Manish" in employees)
# This is extremely useful
if "Neeraj" in employees:
    print("Employee found")

# not in
if "Rahul" not in employees:
    print("Manish is not in the list")

# index() — Find Position
position = employees.index("Neeraj")
print("Neeraj position is : ", position)
# Safer code (ValueError if the value doesn't exist)
if "Rahul" in employees:
    print(employees.index("Rahul"))

# count() — Count Occurrences (Useful when duplicate values are allowed.)
numbers = [10, 20, 20, 30, 20]
print("Count of 20 : ", numbers.count(20))

# sort() — Sort a List
numbers = [50, 10, 40, 20, 30]
numbers.sort()  # Ascending
numbers.sort(reverse=True)  # Descending
print(numbers)
employees.sort()
print(employees)

# reverse() — Reverse a List (does not sort)
employees.reverse()
print(employees)

# copy() — Copy a List (when you want a separate list)
new_employees = employees.copy()
print(new_employees)

# Important: = Does Not Copy a List
employees_1 = employees  # Now both variables point to the same list.

# Loop Through a List
for emp in employees:
    print(emp)

# List with enumerate() (if you need the index)
for index, emp in enumerate(employees):
    print(index, emp)
# Start numbering from 1:
for index, employee in enumerate(employees, start=1):
    print(index, employee)

# List Slicing
print(employees[0:3])  # or print(employees[:3])  # First three
# From index 2
print(employees[2:])
# Last two
print(employees[-2:])
# Reverse
print(employees[::-1])


# List Comprehension
# List comprehension is a very Pythonic way of creating lists.
numbers = []
for number in range(1, 6):
    numbers.append(number * 2)
print(numbers)
# or can write
numbers = [number * 2 for number in range(1, 6)]
print(numbers)

# With a condition
numbers = [1, 2, 3, 4, 5, 6]
even_numbers = [number for number in numbers if number % 2 == 0]
print(even_numbers)


numbers = [10, 20, 30, 40]

print(len(numbers))
print(min(numbers))
print(max(numbers))
print(sum(numbers))
print(20 in numbers)

# sort() vs sorted()
numbers = [30, 10, 20]
numbers.sort() # Changes the original list
print(numbers)

sorted_numbers = sorted(numbers) # Creates and returns a new sorted list
print(numbers)
print(sorted_numbers)