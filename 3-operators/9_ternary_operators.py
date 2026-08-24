# Conditional Expression / Ternary Operator

# Syntax
# value_if_true if condition else value_if_false

age = 20
status = "Adult" if age >= 18 else "Minor"
print(status)

# Equivalent normal if statement:
age = 17
if age >= 18:
    status = "Adult"
else:
    status = "Minor"
print(status)
