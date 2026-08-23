# A dictionary stores data as key-value pairs
# Dictionaries are mutable, so you can add data

# Dictionary Structure : syntax

# dictionary_name = {
#     key: value,
#     key: value,
#     key: value,
# }

# A dictionary can contain different types of values.
user_data = {
    "name": "Vikrant",  # str
    "age": 39,  # int
    "height": 5.10,  # float
    "active": True,  # bool
    "skills": ["Python", "JS"],  # list
}

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
user.update(
    {
        "city": "Gurugram",
        "occupation": "AI Engineer",
    }
)
print(user)
# You can also add new keys with update()
user.update(
    {
        "course": "Python",
    }
)
print(user)


# pop() - Removing a Key (removes a key and returns its value)
city = user.pop("city")
print(city)
print(user)
# pop() With a Default Value (If "city" doesn't exist, it returns N/A instead of raising KeyError)
city = user.pop("city", "N/A")
print(city)
print(user)

# popitem() - removes and returns the last inserted key-value pair.
item = user.popitem()
print(item)
print(user)


# del - remove a dictionary key
del user["occupation"]
print(user)
# pop() returns the removed value, del just removes it.

# clear() - Remove everything
user.clear()
print(user)

# in - Check if a Key Exists
user = {
    "name": "Vikrant",
    "age": 39,
}
print("city" in user)
print("name" in user)

# Check if a Key Does NOT Exist
if "city" not in user:
    print("City is not available")

# keys() - returns the dictionary's keys
print(user.keys())
# loop through keys
for key in user.keys():
    print(key)
# or
for key in user:
    print(key)

# values() - gives the values
for value in user.values():
    print(value)

# items() - gives the both key and value
for key, value in user.items():
    print(key, value)


# Dictionary Values Can Be Almost Anything
data = {
    "name": "Vikrant",
    "skills": ["Python", "React"],
    "address": {
        "city": "Chandigarh",
        "country": "India",
    },
    "scores": (90, 95, 88),
}
print(data)

# Nested Dictionaries
nested = {
    "name": "Vikrant",
    "address": {
        "city": "Chandigarh",
        "country": "India",
    },
}
print(nested)
print(nested["address"]["city"])

# List of Dictionaries (extremely important for API development)
user_list = [
    {
        "id": 1,
        "name": "Ankit",
        "age": 30,
    },
    {
        "id": 2,
        "name": "Manish",
        "age": 35,
    },
    {
        "id": 3,
        "name": "Neeraj",
        "age": 32,
    },
]
print(user_list)
print(user_list[0])
print(user_list[0]["name"])
# Loop through users
for user in user_list:
    print(user["id"], user["name"])


# Dictionary Comprehension
numbers = [1, 2, 3, 4, 5]
squares = {number: number**2 for number in numbers}
print("squares : ", squares)

# Dictionary fromkeys() - create a dictionary from a collection of keys
keys = ["name", "age", "city"]
user = dict.fromkeys(keys)
print(user)
user = dict.fromkeys(keys, "Unknown")

# setdefault() - is useful when want to get a value and create the key if it doesn't exist.
user = {
    "name": "Vikrant",
}
age = user.setdefault("age", "39")
print("Age : ", age)
print("User : ", user)

# len() - Dictionary Length
user = {
    "name": "Vikrant",
    "age": 39,
    "city": "Chandigarh",
}
print("Length : ", len(user))

#  .copy() - Copying a Dictionary (shallow copy)
new_user = user.copy()
# The outer dictionaries are separate, but nested mutable objects such as the skills list can still be shared.

# Deep Copy
# completely independent nested data, Python provides deepcopy()
from copy import deepcopy

new_user = deepcopy(user)

# Quick reference
# | Operation        | Purpose                     |
# | ---------------- | --------------------------- |
# | `d[key]`         | Access value                |
# | `d.get(key)`     | Safely access value         |
# | `d[key] = value` | Add/update                  |
# | `d.update()`     | Add/update multiple         |
# | `d.pop(key)`     | Remove key and return value |
# | `d.popitem()`    | Remove last inserted pair   |
# | `del d[key]`     | Delete key                  |
# | `d.clear()`      | Remove everything           |
# | `d.keys()`       | Get keys                    |
# | `d.values()`     | Get values                  |
# | `d.items()`      | Get key-value pairs         |
# | `d.copy()`       | Shallow copy                |
# | `d.setdefault()` | Get/create default          |
# | `len(d)`         | Number of pairs             |
