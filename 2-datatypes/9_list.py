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

