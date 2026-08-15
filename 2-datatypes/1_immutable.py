"""Demonstrate immutable objects in Python."""

count = 10

print(f"Initial Value: {count}")
print(f"Initial ID: {id(count)}")

count = 120

print(f"After change Value: {count}")
print(f"After change ID: {id(count)}")