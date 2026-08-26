"""A while loop repeats as long as a condition is True"""

# Syntax:

# while condition:
#     code

# How while Works

# count = 1

#      │
#      ▼
# count <= 5?
#      │
#    True
#      │
#      ▼
#  print(count)
#      │
#      ▼
# count += 1
#      │
#      └──────────────┐
#                     │
#                     ▼
#               Check again

count = 1
while count <= 5:
    print(count)
    count += 1


# for vs while

# for
#  ↓
# "Give me each item"

# while
#  ↓
# "Keep going while this condition is true"

# Infinite while Loop

# while True:
#     print("Hello")
# This never ends on its own

while True:
    command = input("Enter command (exit to break): ")
    if command == "exit":
        break

