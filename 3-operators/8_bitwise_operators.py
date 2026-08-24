# Bitwise operators work at the binary/bit level of integers.

# These are more advanced but important for interviews and low-level programming.
# Python provides:

# &    AND
# |    OR
# ^    XOR
# ~    NOT
# <<   Left shift
# >>   Right shift

# & Bitwise AND
a = 5
b = 3

# Binary

# 5 = 101
# 3 = 011

# AND

#   101
# & 011
# -----
#   001

print(5 & 3)
# Output: 1

# | Bitwise OR
print(5 | 3)

# Binary

#   101
# | 011
# -----
#   111

# 111 in decimal is 7
# Output : 7

# ^ Bitwise XOR (returns 1 when the bits are different)
print(5 ^ 3)

#   101
# ^ 011
# -----
#   110

# Output : 6

# ~ Bitwise NOT
print(~5)

# << Left Shift
print(5 << 1)

# 101
#  ↓ shift left
# 1010

# >> Right Shift
print(5 >> 1)

# 101
#  ↓ shift right
# 10

# Bitwise Operator Summary

# | Operator | Name        | Example  | 
# | -------- | ----------- | -------- | 
# | `&`      | AND         | `5 & 3`  | 
# | `        | `           | OR       | 
# | `^`      | XOR         | `5 ^ 3`  | 
# | `~`      | NOT         | `~5`     | 
# | `<<`     | Left shift  | `5 << 1` | 
# | `>>`     | Right shift | `5 >> 1` | 
