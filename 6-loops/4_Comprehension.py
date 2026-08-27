# List Comprehension

# Python provides a concise way to create lists using iteration and optional conditions.

# Normal loop:
numbers = [1, 2, 3, 4, 5]
squares = []
for number in numbers:
    squares.append(number ** 2)
    
# List comprehension:
squares = [number ** 2 for number in numbers]
print(squares)

# List Comprehension With Condition

# Normal:
even_numbers = []
for number in numbers:
    if number % 2 == 0:
        even_numbers.append(number)
        

# Comprehension:
even_numbers = [
    number
    for number in numbers
    if number % 2 == 0
]


# Dictionary Comprehension

# You can also create dictionaries.
numbers = [1, 2, 3, 4]
squares = {
    number: number ** 2
    for number in numbers
}
print(squares)

# Set Comprehension

# You can create sets:
numbers = [1, 2, 2, 3, 3, 4]
unique_squares = {
    number ** 2
    for number in numbers
}
print(unique_squares)
