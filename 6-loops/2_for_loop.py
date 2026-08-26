"""The for loop is used when you want to iterate over an iterable"""

# An iterable can be:

# list
# tuple
# string
# set
# dictionary
# range
# file
# generator

#  syntax:
#      for variable in iterable:
#     # code

names = ["Ankit", "Manish", "Neeraj"]
for name in names:
    print(name)
# Python automatically takes each element one by one

# Loop Through a String (useful when processing individual characters)
name = "Python"
for character in name:
    print(character)

# Loop Through a Tuple
employees = ("Ankit", "Manish", "Neeraj")
for employee in employees:
    print(employee)

# Loop Through a Set (Remember that a set is not indexed, so don't depend on a particular order)
skills = {"Python", "React", "Node.js"}
for skill in skills:
    print(skill)

# Loop Through a Dictionary
user = {
    "name": "Vikrant",
    "age": 41,
    "city": "Chandigarh",
}
# Loop through keys
for key in user:
    print(key)

# Loop through values
for value in user.values():
    print(value)

# Loop through key-value pairs
for key, value in user.items():
    print(key, value)

# range() - is one of the most commonly used tools with for
for number in range(5):
    print(number)
    # Important: range(5) starts at 0 and stops before 5

# range(start, stop)
for number in range(1, 6):
    print(number)
# Notice:
# start = 1
# stop  = 6
# But 6 is not included

# range(start, stop, step)
for number in range(1, 11, 2):
    print(number)

# Counting Backwards
for number in range(10, 0, -1):
    print("count down : ", number)

# for Loop + Condition
numbers = [1, 2, 3, 4, 5, 6]
for number in numbers:
    if number % 2 == 0:
        print(number, " is even")
        

# break - immediately terminates the loop
for number in range(1, 11):
    if number == 5:
        break

    print(number)

# Suppose search for a user:
users = ["Ankit", "Manish", "Neeraj", "Rahul"]
for user in users:
    if user == "Neeraj":
        print("User found")
        break

# continue - skips the current iteration and moves to the next one
for number in range(1, 6):
    if number == 3:
        continue
    print(number)

# break vs continue

# break
#  ↓
# Stop the entire loop


# continue
#  ↓
# Skip current iteration
#  ↓
# Continue with next iteration

for number in range(1, 6):
    if number == 3:
        continue
    if number == 5:
        break
    print(number)

# pass - does nothing (It is useful when Python requires a statement but you don't want to implement the logic yet)
for number in range(5):
    if number == 1:
        pass
    if number == 2:
        continue
    if number == 4:
        break
    print(number)

# Loop else (The else block executes when the loop completes normally, without break)
# for ...:
#     ...
# else:
#     ...

for number in range(5):
    print(number)
else:
    print("Loop completed")

# Loop else With break

numbers = [10, 20, 30, 40]
for number in numbers:
    if number == 30:
        print("Found")
        break
else:
    print("Not found")
# The else doesn't execute because break interrupted the loop
# Found?
#  ├── Yes → break → "Found"
#  └── No  → loop finishes → "Not found"


# Nested Loops - A loop inside another loop is called a nested loop
for i in range(3):
    for j in range(3):
        print(i, j)

# Nested loops are also common in:
# matrices
# grids
# game boards
# comparisons
# combinations
# multidimensional data

# enumerate() - want both the index and value
employees = ["Ankit", "Manish", "Neeraj"]
for index, employee in enumerate(employees):
    print(index, employee)

# Start enumerate() From Another Number
for index, employee in enumerate(employees, start=1):
    print(index, employee)


# zip() lets you iterate over multiple collections simultaneously

names = ["Ankit", "Manish", "Neeraj"]
ages = [30, 35, 32]
for name, age in zip(names, ages):
    print(name, age)

# By default, zip() stops at the shortest iterable (if Lists Have Different Lengths)
names = ["Ankit", "Manish", "Neeraj"]
ages = [30, 35]
for name, age in zip(names, ages):
    print(name, age)

# In modern Python, you can request strict matching, This raises an error if the lengths don't match
# for name, age in zip(names, ages, strict=True):
#     print(name, age)
