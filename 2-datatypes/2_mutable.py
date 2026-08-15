"""Demonstrate mutable objects in Python."""

employees = set()

print(f"initial value : {employees}")
print(f"initial ID : {id(employees)}")

employees.add("Vikrant")
employees.add("Kumar")

print(f"After change value : {employees}")
print(f"After change ID : {id(employees)}")