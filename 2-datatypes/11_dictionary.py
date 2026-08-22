# A dictionary stores data as key-value pairs
# Dictionaries are mutable, so you can add data

# Dictionary Structure : syntax

# dictionary_name = {
#     key: value,
#     key: value,
#     key: value,
# }

user = {
    "name": "Vikrant",
    "country": "India",
    "occupation": " Software Engineer",
}
print(user)
# can also create an empty dictionary
user_1 = {}
# or
user_2 = dict()

# Accessing Values
print("Name : ", user["name"])
print("Country : ", user["country"])

# get() — Safely Access a Value (Give me this value if it exists; otherwise return None)

# print("City : ",user["city"]) # KeyError because "city" doesn't exist.
print("City : ", user.get("city"))
# You can also provide a default
print("City : ", user.get("city", "Unknown"))

# Adding a New Key
user["city"] = "Chandigarh"
print(user)

# Updating a Value (If the key already exists, assigning a value changes it)
user["city"] = "Delhi"
print(user)

# The important distinction:

# Key doesn't exist
#        ↓
# Assignment adds it

# Key already exists
#        ↓
# Assignment updates it


# update() — Update Multiple Values ()
user.update({
    "city": "Gurugram",
    "occupation": "AI Engineer",
})
print(user)
# You can also add new keys with update()
user.update({
    "course": "Python",
})
print(user)


# pop() - Removing a Key (removes a key and returns its value)
