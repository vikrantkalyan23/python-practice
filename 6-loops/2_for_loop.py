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
    print("count down : ",number)

# for Loop + Condition
numbers = [1, 2, 3, 4, 5, 6]
for number in numbers:
    if number % 2 == 0:
        print(number," is even")