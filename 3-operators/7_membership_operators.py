# Membership operators check whether a value exists inside a collection

# in
# not in

# in
employees = ["Ankit", "Manish", "Neeraj"]
print("Manish" in employees)

# not in
print("Rahul" not in employees)

# Membership with Strings
message = "Hello Python"
print("Python" in message)
print("Java" not in message)

# Membership with Dictionaries (it does not search dictionary values)
user = {
    "name": "Vikrant",
    "age": 39,
}
print("name" in user)
