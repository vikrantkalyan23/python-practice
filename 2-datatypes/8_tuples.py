"""Tuple is immutable"""

employees = ("Ankit", "Manish", "Neeraj")
emp1, emp2, emp3 = employees
emp1_age, emp2_age, emp3_age = 25, 28, 32

print(f"Employee 2: {emp2} and Age : {emp2_age}")

print(f"Initial Tuple ID : {id(employees)}")

employees = ("Ankit", "Manish", "Neeraj", "Sandeep")

print(f"After change Tuple ID : {id(employees)}")

# Check member in tuple

print(f"is Neeraj exists : {'Neeraj' in employees}")
print(f"is Vikrant exists : {'Vikrant' in employees}")

# Print all members
for employee in employees:
    print(employee)
