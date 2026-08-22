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

#Nested Dictionaries
nested = {
    "name": "Vikrant",
    "address": {
        "city": "Chandigarh",
        "country": "India",
    },
}
print(nested)
print(nested["address"]["city"])

#List of Dictionaries (extremely important for API development)
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
    print(user["id"],user["name"])
     