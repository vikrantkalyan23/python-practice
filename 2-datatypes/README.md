# Python Data Types 

## 1. What are Data Types?

A **data type** tells Python what kind of value a variable contains.

``` python
name = "Vikrant"
age = 41
height = 5.10
is_active = True
```

Python understands these as:

``` text
name       → str
age        → int
height     → float
is_active  → bool
```

Check a value's type with `type()`:

``` python
print(type(name))
print(type(age))
print(type(height))
print(type(is_active))
```

------------------------------------------------------------------------

## 2. Main Python Data Types

  Category   Type          Example
  ---------- ------------- -----------------------
  Numeric    `int`         `10`
  Numeric    `float`       `10.5`
  Numeric    `complex`     `2 + 3j`
  Boolean    `bool`        `True`
  Text       `str`         `"Hello"`
  Sequence   `list`        `[1, 2, 3]`
  Sequence   `tuple`       `(1, 2, 3)`
  Sequence   `range`       `range(5)`
  Set        `set`         `{1, 2, 3}`
  Mapping    `dict`        `{"name": "Vikrant"}`
  Binary     `bytes`       `b"Hello"`
  Binary     `bytearray`   `bytearray(b"Hello")`
  Special    `NoneType`    `None`

For beginners, focus first on:

``` text
int → float → bool → str → list → tuple → set → dict → None
```

------------------------------------------------------------------------

# 3. Integer --- `int`

An integer is a whole number without a decimal part.

``` python
age = 41
quantity = 10
temperature = -5
year = 2026
```

Check the type:

``` python
age = 41

print(age)
print(type(age))
```

Output:

``` text
41
<class 'int'>
```

### Integer operations

``` python
a = 10
b = 3

print(a + b)   # 13
print(a - b)   # 7
print(a * b)   # 30
print(a / b)   # 3.333...
print(a // b)  # 3
print(a % b)   # 1
print(a ** b)  # 1000
```

  Operator   Meaning
  ---------- ----------------
  `+`        Addition
  `-`        Subtraction
  `*`        Multiplication
  `/`        Division
  `//`       Floor division
  `%`        Remainder
  `**`       Power

------------------------------------------------------------------------

# 4. Float --- `float`

A float represents a number with a decimal point.

``` python
price = 99.99
height = 5.10
temperature = -2.5
```

``` python
price = 99.99

print(price)
print(type(price))
```

Output:

``` text
99.99
<class 'float'>
```

------------------------------------------------------------------------

# 5. Complex --- `complex`

Python supports complex numbers.

``` python
number = 2 + 3j

print(number)
print(type(number))
```

Output:

``` text
(2+3j)
<class 'complex'>
```

Access the real and imaginary parts:

``` python
print(number.real)
print(number.imag)
```

Complex numbers are mostly useful in mathematics, engineering, and
scientific computing.

------------------------------------------------------------------------

# 6. Boolean --- `bool`

A Boolean has only two values:

``` python
True
False
```

Example:

``` python
is_logged_in = True
is_admin = False
```

Booleans are commonly used in conditions:

``` python
age = 20

is_adult = age >= 18

print(is_adult)
```

Output:

``` text
True
```

------------------------------------------------------------------------

# 7. String --- `str`

A string represents text.

``` python
name = "Vikrant"
city = "Chandigarh"
message = "Hello Python"
```

You can use either:

``` python
"Hello"
```

or:

``` python
'Hello'
```

### Concatenation

``` python
first_name = "Vikrant"
last_name = "Kalyan"

full_name = first_name + " " + last_name

print(full_name)
```

Output:

``` text
Vikrant Kalyan
```

### Length

``` python
language = "Python"

print(len(language))
```

Output:

``` text
6
```

------------------------------------------------------------------------

# 8. String Indexing

Python strings use zero-based indexing.

``` text
 P  y  t  h  o  n
 0  1  2  3  4  5
```

``` python
language = "Python"

print(language[0])
print(language[1])
print(language[5])
```

Output:

``` text
P
y
n
```

Negative indexes count from the end:

``` python
print(language[-1])
```

Output:

``` text
n
```

------------------------------------------------------------------------

# 9. String Slicing

Slicing extracts part of a string.

``` python
language = "Python"

print(language[0:3])
```

Output:

``` text
Pyt
```

General form:

``` python
value[start:stop]
```

The `stop` position is not included.

``` python
print(language[0:2])  # Py
print(language[2:5])  # tho
```

------------------------------------------------------------------------

# 10. List --- `list`

A list stores multiple values in an ordered collection.

``` python
fruits = ["apple", "banana", "orange"]
```

A list can contain different types:

``` python
items = ["Python", 10, 20.5, True]
```

Check the type:

``` python
print(type(fruits))
```

Output:

``` text
<class 'list'>
```

------------------------------------------------------------------------

# 11. Lists are Mutable

**Mutable** means an object can be changed after it is created.

``` python
fruits = ["apple", "banana", "orange"]

fruits[0] = "mango"

print(fruits)
```

Output:

``` text
['mango', 'banana', 'orange']
```

Add an item:

``` python
fruits.append("grapes")
```

Remove an item:

``` python
fruits.remove("banana")
```

Other useful methods:

``` python
fruits.sort()
fruits.reverse()
print(len(fruits))
```

------------------------------------------------------------------------

# 12. Tuple --- `tuple`

A tuple is an ordered collection similar to a list.

``` python
coordinates = (10, 20)

print(coordinates)
print(type(coordinates))
```

Tuples are normally used for data that should not be changed.

## Tuples are Immutable

``` python
coordinates = (10, 20)

# This causes an error:
# coordinates[0] = 100
```

Main difference:

``` text
list
  ↓
mutable
  ↓
can be changed

tuple
  ↓
immutable
  ↓
cannot be changed
```

------------------------------------------------------------------------

# 13. Set --- `set`

A set stores unique values.

``` python
numbers = {1, 2, 3, 4}
```

Duplicates are removed:

``` python
numbers = {1, 2, 2, 3, 3, 4}

print(numbers)
```

The result contains each value only once.

Sets are useful when you need **unique values**.

``` python
skills = {"Python", "JavaScript", "Python", "SQL"}

print(skills)
```

`Python` is stored only once.

------------------------------------------------------------------------

# 14. Dictionary --- `dict`

A dictionary stores data as **key-value pairs**.

``` python
user = {
    "name": "Vikrant",
    "age": 41,
    "city": "Chandigarh",
}
```

Think of it as:

``` text
key       value
----------------
name      Vikrant
age       41
city      Chandigarh
```

Access values:

``` python
print(user["name"])
print(user["age"])
```

Output:

``` text
Vikrant
41
```

Dictionaries are mutable:

``` python
user["age"] = 42
user["country"] = "India"
```

------------------------------------------------------------------------

# 15. `None` --- `NoneType`

`None` represents the absence of a value.

``` python
result = None

print(result)
print(type(result))
```

Output:

``` text
None
<class 'NoneType'>
```

Example:

``` python
user = None

if user is None:
    print("No user found")
```

Prefer:

``` python
user is None
```

instead of:

``` python
user == None
```

------------------------------------------------------------------------

# 16. Range --- `range`

`range` represents a sequence of numbers and is commonly used with
loops.

``` python
for number in range(5):
    print(number)
```

Output:

``` text
0
1
2
3
4
```

The ending value `5` is not included.

------------------------------------------------------------------------

# 17. Bytes --- `bytes`

`bytes` is used for binary data.

``` python
data = b"Hello"

print(data)
print(type(data))
```

You may encounter bytes when working with files, images, network
communication, encryption, and binary protocols.

For beginner web development, learn this later.

------------------------------------------------------------------------

# 18. Bytearray --- `bytearray`

`bytearray` is similar to `bytes`, but it is mutable.

``` python
data = bytearray(b"Hello")

print(data)
print(type(data))
```

This is an advanced data type for beginners and can be learned later.

------------------------------------------------------------------------

# 19. Mutable vs Immutable

This is an important Python concept.

## Mutable types

These can be changed after creation:

``` text
list
dict
set
bytearray
```

Example:

``` python
numbers = [1, 2, 3]

numbers[0] = 100

print(numbers)
```

Output:

``` text
[100, 2, 3]
```

## Immutable types

These cannot be changed after creation:

``` text
int
float
bool
str
tuple
bytes
```

Example:

``` python
name = "Python"

# Strings are immutable.
# Reassignment makes the variable refer to another string object.
name = "Java"
```

### Important

Don't say:

> "The variable is immutable."

More accurately:

> **The object is immutable.**

A variable can be reassigned to another object.

------------------------------------------------------------------------

# 20. Demonstrating `id()`

Python's `id()` returns an identity value for an object during its
lifetime.

This can help demonstrate mutability.

## Integer

``` python
count = 10

print("Before:", count)
print("ID:", id(count))

count = 120

print("After:", count)
print("ID:", id(count))
```

The integer object is immutable. Assigning `120` makes `count` refer to
an integer object representing `120`.

## List

``` python
numbers = [1, 2, 3]

print("Before:", numbers)
print("ID:", id(numbers))

numbers[0] = 100

print("After:", numbers)
print("ID:", id(numbers))
```

The list itself was modified.

> Do not rely on the exact numeric value returned by `id()`. Use it to
> understand object identity.

------------------------------------------------------------------------

# 21. `type()`

Use `type()` to inspect a value's type.

``` python
name = "Vikrant"
age = 41
height = 5.10
active = True

print(type(name))
print(type(age))
print(type(height))
print(type(active))
```

------------------------------------------------------------------------

# 22. `isinstance()`

`isinstance()` checks whether an object is an instance of a type.

``` python
age = 41

print(isinstance(age, int))
```

Output:

``` text
True
```

Another example:

``` python
name = "Vikrant"

print(isinstance(name, str))
print(isinstance(name, int))
```

Output:

``` text
True
False
```

For application code, `isinstance()` is often more useful than directly
comparing `type()`.

------------------------------------------------------------------------

# 23. Type Conversion

Python lets you convert values between compatible types.

### String → Integer

``` python
age = "41"

age = int(age)

print(age)
print(type(age))
```

### Integer → String

``` python
age = 41

age = str(age)

print(age)
print(type(age))
```

### String → Float

``` python
price = "99.99"

price = float(price)

print(price)
```

### Integer → Float

``` python
number = 10

result = float(number)

print(result)
```

Be careful: not every conversion is valid.

``` python
# Raises ValueError:
# number = int("hello")
```

------------------------------------------------------------------------

# 24. Important `input()` Example

`input()` returns a string.

``` python
age = input("Enter your age: ")

print(type(age))
```

If the user enters:

``` text
41
```

the type is still:

``` text
str
```

Convert it when you need a number:

``` python
age = int(input("Enter your age: "))

print(type(age))
```

Now the type is:

``` text
int
```

------------------------------------------------------------------------

# 25. Nested Data Types

Python data types can contain other data types.

For example, a list can contain dictionaries:

``` python
users = [
    {
        "name": "Vikrant",
        "age": 41,
    },
    {
        "name": "John",
        "age": 30,
    },
]
```

Access a value:

``` python
print(users[0]["name"])
```

Output:

``` text
Vikrant
```

This pattern is very common when working with JSON and APIs.

------------------------------------------------------------------------

# 26. Real-World Example

Imagine an e-commerce product:

``` python
product_name = "MacBook"
price = 1999.99
quantity = 2
is_available = True

categories = ["Laptop", "Apple", "Electronics"]

product = {
    "name": product_name,
    "price": price,
    "quantity": quantity,
    "available": is_available,
    "categories": categories,
}
```

The types are:

``` text
product_name  → str
price         → float
quantity      → int
is_available  → bool
categories    → list
product       → dict
```

This is similar to the data used in real applications.

------------------------------------------------------------------------

# 27. Quick Reference

``` text
int
    Whole numbers
    Example: 10

float
    Decimal numbers
    Example: 10.5

complex
    Complex numbers
    Example: 2 + 3j

bool
    True / False
    Example: True

str
    Text
    Example: "Python"

list
    Ordered, mutable collection
    Example: [1, 2, 3]

tuple
    Ordered, immutable collection
    Example: (1, 2, 3)

set
    Unique values
    Example: {1, 2, 3}

dict
    Key-value pairs
    Example: {"name": "Vikrant"}

range
    Number sequence
    Example: range(5)

bytes
    Immutable binary data
    Example: b"Hello"

bytearray
    Mutable binary data
    Example: bytearray(b"Hello")

NoneType
    Represents no value
    Example: None
```

------------------------------------------------------------------------

# 28. Recommended Learning Order

Learn these in this order:

``` text
int
 ↓
float
 ↓
bool
 ↓
str
 ↓
list
 ↓
tuple
 ↓
set
 ↓
dict
 ↓
None
 ↓
range
 ↓
bytes / bytearray
```

Then study:

``` text
Indexing
    ↓
Slicing
    ↓
Mutable vs Immutable
    ↓
type()
    ↓
isinstance()
    ↓
Type conversion
    ↓
Nested data
```

------------------------------------------------------------------------

# 29. Practice Program

Create:

``` text
data_types_demo.py
```

Add:

``` python
"""Demonstrate common Python data types."""

name = "Vikrant"
age = 41
height = 5.10
is_developer = True

skills = ["Python", "JavaScript", "NestJS"]
coordinates = (30.7333, 76.7794)
unique_numbers = {1, 2, 3, 3}

user = {
    "name": name,
    "age": age,
    "developer": is_developer,
}

result = None

print("Name:", name)
print("Age:", age)
print("Height:", height)
print("Developer:", is_developer)
print("Skills:", skills)
print("Coordinates:", coordinates)
print("Unique numbers:", unique_numbers)
print("User:", user)
print("Result:", result)

print("\nData Types:")

print(type(name))
print(type(age))
print(type(height))
print(type(is_developer))
print(type(skills))
print(type(coordinates))
print(type(unique_numbers))
print(type(user))
print(type(result))
```

Run:

``` bash
python data_types_demo.py
```

------------------------------------------------------------------------

# 30. Beginner Mental Model

``` text
Python Values
│
├── Numbers
│   ├── int
│   ├── float
│   └── complex
│
├── Boolean
│   └── bool
│
├── Text
│   └── str
│
├── Collections
│   ├── list
│   ├── tuple
│   ├── set
│   ├── dict
│   └── range
│
├── Binary
│   ├── bytes
│   └── bytearray
│
└── Special
    └── None
```

Remember these first:

``` text
int       → 10
float     → 10.5
bool      → True / False
str       → "Hello"
list      → [1, 2, 3]
tuple     → (1, 2, 3)
set       → {1, 2, 3}
dict      → {"name": "Vikrant"}
None      → no value
```

> **Data types are the foundation of Python. Become comfortable
> creating, checking, indexing, modifying, and converting the common
> types before moving to advanced Python.**
