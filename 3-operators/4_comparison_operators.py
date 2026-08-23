# Comparison operators compare two values

# result of Comparison : True/False

# | Operator | Meaning       | Example    |
# | -------- | ------------- | ---------- |
# | `==`     | Equal         | `10 == 10` |
# | `!=`     | Not equal     | `10 != 5`  |
# | `>`      | Greater than  | `10 > 5`   |
# | `<`      | Less than     | `10 < 20`  |
# | `>=`     | Greater/equal | `10 >= 10` |
# | `<=`     | Less/equal    | `10 <= 20` |

a = 10
b = 20

# == Equal To
print(a == b)

# != Not Equal
print(a != b)

# > Greater Than
print(a > b)

# < Less Than
print(a < b)

# >= Greater Than or Equal To
age = 18
print(age >= 18)

# <= Less Than or Equal To
print(age <= 18)

age = 21
if age >= 18:
    print("Eligible")
else:
    print("Not eligible")
