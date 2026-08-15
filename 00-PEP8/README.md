# PEP 8 --- Python Style Guide for Beginners

## 1. What is PEP 8?

**PEP 8** means **Python Enhancement Proposal 8**.

It is Python's style guide. It explains how we should format and
organize Python code so that it is:

-   Easy to read
-   Easy to understand
-   Consistent
-   Easier to maintain
-   Easier for teams to work on together

Think of PEP 8 as a set of **good coding habits for Python**.

> PEP 8 is mostly about readability and consistency. It usually does not
> change what your program does.

------------------------------------------------------------------------

## 2. Why is PEP 8 Important?

Imagine two developers write code that does exactly the same thing.

### Hard to read

``` python
def add(a,b):
 x=a+b
 return x
```

### Easy to read

``` python
def add(a, b):
    result = a + b
    return result
```

Both work, but the second version is easier to understand.

That is the main purpose of PEP 8.

------------------------------------------------------------------------

# 3. Indentation

Python uses indentation to define blocks of code.

PEP 8 recommends **4 spaces** for each indentation level.

### Bad

``` python
if age >= 18:
  print("Adult")
```

### Good

``` python
if age >= 18:
    print("Adult")
```

Do not mix tabs and spaces.

------------------------------------------------------------------------

# 4. Spaces Around Operators

Use spaces around operators such as:

-   `=`
-   `+`
-   `-`
-   `*`
-   `/`
-   `==`
-   `>`

### Bad

``` python
total=price+tax
```

### Good

``` python
total = price + tax
```

------------------------------------------------------------------------

# 5. Spaces After Commas

Use a space after commas.

### Bad

``` python
user = User("Vikrant","India",40)
```

### Good

``` python
user = User("Vikrant", "India", 40)
```

------------------------------------------------------------------------

# 6. Variable Names

Use **snake_case** for variables.

### Good

``` python
user_name = "Vikrant"
total_price = 500
first_name = "John"
```

### Avoid

``` python
userName = "Vikrant"
TotalPrice = 500
```

Python normally uses:

``` text
snake_case
```

instead of:

``` text
camelCase
```

for variables and functions.

------------------------------------------------------------------------

# 7. Function Names

Use **snake_case** for functions.

### Good

``` python
def calculate_total():
    pass


def get_user_by_id():
    pass
```

### Avoid

``` python
def calculateTotal():
    pass
```

------------------------------------------------------------------------

# 8. Class Names

Use **PascalCase** for classes.

### Good

``` python
class User:
    pass


class UserAccount:
    pass


class PaymentService:
    pass
```

### Avoid

``` python
class user:
    pass
```

------------------------------------------------------------------------

# 9. Constants

Constants are normally written in **UPPER_CASE**.

``` python
MAX_RETRIES = 3
DEFAULT_TIMEOUT = 30
DATABASE_NAME = "myapp"
```

This tells other developers:

> "This value is intended to be treated as a constant."

------------------------------------------------------------------------

# 10. File and Module Names

Python module names should normally be lowercase.

Good:

``` text
user.py
database.py
user_service.py
payment_service.py
```

Avoid unnecessary names like:

``` text
UserService.py
USER_SERVICE.py
```

------------------------------------------------------------------------

# 11. Line Length

Traditionally, PEP 8 recommends keeping code lines around **79
characters or fewer**.

Instead of making one very long line:

``` python
user = User(name="Vikrant", email="vikrant@example.com", age=40, active=True)
```

you can write:

``` python
user = User(
    name="Vikrant",
    email="vikrant@example.com",
    age=40,
    active=True,
)
```

Modern projects may use tools such as **Black** or **Ruff** with their
own configured line length.

The important idea is:

> Keep code readable.

------------------------------------------------------------------------

# 12. Blank Lines

Use blank lines to separate different parts of your code.

``` python
import os
import sys


class User:
    pass


def create_user():
    pass
```

Generally:

-   Use **2 blank lines** around top-level classes and functions.
-   Use **1 blank line** between methods inside a class.

------------------------------------------------------------------------

# 13. Imports

Put imports near the top of the file.

### Good

``` python
import os
import sys

import requests

from myapp.services import UserService
```

A common organization is:

``` text
1. Standard library
2. Third-party packages
3. Your application code
```

------------------------------------------------------------------------

# 14. Avoid Wildcard Imports

Avoid:

``` python
from math import *
```

Prefer:

``` python
import math

result = math.sqrt(25)
```

or:

``` python
from math import sqrt

result = sqrt(25)
```

The second approach makes it easier to understand where something came
from.

------------------------------------------------------------------------

# 15. Comments

Comments should help explain code.

### Not very useful

``` python
# Add 1 to count
count += 1
```

The code already tells us that.

### More useful

``` python
# Retry because the external API can temporarily return HTTP 503.
count += 1
```

A good comment often explains **why**, not just **what**.

------------------------------------------------------------------------

# 16. Boolean Comparisons

Avoid unnecessary comparisons with `True` and `False`.

### Bad

``` python
if is_active == True:
    print("Active")
```

### Good

``` python
if is_active:
    print("Active")
```

For false:

``` python
if not is_active:
    print("Inactive")
```

------------------------------------------------------------------------

# 17. Avoid Unnecessary Complexity

### Too complicated

``` python
if user_exists == True:
    return True
else:
    return False
```

### Simple

``` python
return user_exists
```

Simple code is usually easier to maintain.

------------------------------------------------------------------------

# 18. Use Meaningful Names

### Bad

``` python
x = 500
y = 20
z = x + y
```

### Better

``` python
price = 500
tax = 20
total_price = price + tax
```

Meaningful names make code easier to understand.

------------------------------------------------------------------------

# 19. Exception Handling

Do not silently ignore errors.

### Bad

``` python
try:
    process_payment()
except Exception:
    pass
```

This can hide important problems.

### Better

``` python
try:
    process_payment()
except PaymentError as error:
    print(f"Payment failed: {error}")
    raise
```

Handle errors intentionally.

------------------------------------------------------------------------

# 20. A Complete PEP 8 Example

### Before

``` python
import os
class user:
 def __init__(self,name,email):
  self.name=name
  self.email=email
 def getUserName(self):
  return self.name
```

### After

``` python
import os


class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email

    def get_user_name(self):
        return self.name
```

The second version follows common PEP 8 conventions.

------------------------------------------------------------------------

# 21. PEP 8 Quick Reference

  Item          Recommended Style
  ------------- ---------------------------------
  Indentation   4 spaces
  Variables     `snake_case`
  Functions     `snake_case`
  Classes       `PascalCase`
  Constants     `UPPER_CASE`
  Modules       `lowercase`
  Operators     Spaces around operators
  Commas        Space after comma
  Imports       At the top
  Comments      Explain useful context
  Code          Prefer readable and simple code

------------------------------------------------------------------------

# 22. PEP 8 in One Sentence

> **PEP 8 helps Python developers write code that is consistent, clean,
> and easy to read.**

------------------------------------------------------------------------

# 23. Beginner Rule

When you are starting Python, remember these five rules first:

``` text
1. Use 4 spaces for indentation.
2. Use snake_case for variables and functions.
3. Use PascalCase for classes.
4. Put spaces around operators.
5. Write code for humans to read, not only for the computer.
```

Once these become habits, learn the rest of PEP 8 gradually.
