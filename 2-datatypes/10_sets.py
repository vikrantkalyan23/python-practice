# A set is a built-in Python data type used to store a collection of unique values.
# Set
#  │
#  ├── Unique values
#  ├── Mutable
#  ├── No indexing
#  ├── Fast membership checking
#  └── Supports mathematical set operations

# Most Important Things to Remember
# 1. Set stores unique values.
# 2. Set is mutable.
# 3. Set does not support indexing.
# 4. Set is excellent for membership checking.
# 5. Set automatically removes duplicates.
# 6. add() → one item
# 7. update() → multiple items
# 8. remove() → error if missing
# 9. discard() → safe remove
# 10. pop() → arbitrary element
# 11. | → union
# 12. & → intersection
# 13. - → difference
# 14. ^ → symmetric difference

# Creating a Set - Use curly braces {}
set_1 = {10, 20, 30}
print(set_1)
print(type(set_1))

# To create an empty set
items = {}  # It creates an empty dictionary.
print(type(items))

items = set()  # empty set
print(type(items))

# Sets Don't Allow Duplicates
numbers = {10, 20, 20, 30, 30, 40}
print("Duplicate : ", numbers)  # The duplicate values are automatically removed

# Sets Are Mutable (can add and remove items from a set)
skills = {"Python", "JavaScript"}
skills.add("React")
print("Add 1 item : ", skills)

# update() — Add Multiple Items (add multiple values)
skills.update(["Nextjs", "Nestjs"])
print("Add multiple items : ", skills)
skills.update({"Mysql", "PostgreSQL"})
print("Add multiple items : ", skills)

# remove() — Remove an Item (If the item doesn't exist: KeyError)
skills.remove("React")
print("Remove 1 item : ", skills)

# discard() — Safer Remove (removes an item if it exists.)
skills.discard("Java")
print("Remove 1 item by discard : ", skills)

# pop() — Remove an Item (removes an arbitrary element.)
removed_skill = skills.pop()
print("POP item :", removed_skill)
print(skills)


# Quick comparison
# | Method       | What it does              | If item doesn't exist |
# | ------------ | ------------------------- | --------------------- |
# | `pop()`      | Removes an arbitrary item | `KeyError` if empty   |
# | `remove(x)`  | Removes specific item     | `KeyError`            |
# | `discard(x)` | Removes specific item     | No error              |

# clear() — Remove Everything
skills_1 = {"Python", "JavaScript", "React"}
skills_1.clear()
print("Clear : ", skills_1)


# Checking Membership
print("Python" in skills)

# Loop Through a Set
for s in skills:
    print(s)

# If need sorted output:
for skill in sorted(skills):
    print(skill)

# Mathematical Set Operations
backend = {"Python", "Node.js", "Java"}
frontend = {"JavaScript", "React", "Node.js"}

# Union — | (Remove Duplicate)
all_skills = backend | frontend
print("All by | : ", all_skills)
# or
all_s = backend.union(frontend)
print("All by union : ", all_s)

# Intersection — & (values exist in both sets)
common_skills = backend & frontend
print("common by & : ", common_skills)
# or
common_s = backend.intersection(frontend)
print("common by intersection: ", common_s)

# Difference — - (exists in the first set but not the second)
backend_only = backend - frontend
print("Backend Only : ", backend_only)
frontend_only = frontend - backend
print("Frontend Only : ", frontend_only)

# Symmetric Difference — ^ (Give me values that exist in either set, but not in both)
different_skills = backend ^ frontend
print("Symmetric Difference : ", different_skills)

# Subset — <=  (A set is a subset if all of its elements exist in another set)
backend = {"Python", "Node.js", "Java"}
python_stack = {"Python", "Node.js"}
print("python_stack is subset of backend : ",python_stack <= backend)
# or
python_stack.issubset(backend)
print("python_stack is subset of backend using issubset : ",python_stack.issubset(backend))

# Superset — >=
print("backend is superset of python_stack : ",  backend >= python_stack)
print("backend is superset of python_stack : ",  backend.issuperset(python_stack))

# Disjoint Sets (Two sets are disjoint when they have no common elements)
frontend = {"React", "Next.js"}
backend = {"Python", "Django"}

print("Disjoint Set : ",frontend.isdisjoint(backend))

# Common Set Methods

# | Method                   | Purpose                       |
# | ------------------------ | ----------------------------- |
# | `add()`                  | Add one item                  |
# | `update()`               | Add multiple items            |
# | `remove()`               | Remove item, error if missing |
# | `discard()`              | Remove item safely            |
# | `pop()`                  | Remove an arbitrary item      |
# | `clear()`                | Remove everything             |
# | `union()`                | Combine sets                  |
# | `intersection()`         | Common items                  |
# | `difference()`           | Items only in first set       |
# | `symmetric_difference()` | Items in either, but not both |
# | `issubset()`             | Check subset                  |
# | `issuperset()`           | Check superset                |
# | `isdisjoint()`           | Check no common items         |


# Set vs List

# | Feature                 | List               | Set                                    |
# | ----------------------- | ------------------ | -------------------------------------- |
# | Syntax                  | `[]`               | `{}`                                   |
# | Ordered                 | Yes                | No indexing/order guarantee to rely on |
# | Mutable                 | Yes                | Yes                                    |
# | Duplicates              | Allowed            | Not allowed                            |
# | Indexing                | Yes                | No                                     |
# | Slicing                 | Yes                | No                                     |
# | Membership              | O(n) average       | O(1) average                           |
# | Main purpose            | Ordered collection | Unique values / membership             |
# | Mathematical operations | No                 | Yes                                    |


# Set vs Tuple

# | Feature          | Set           | Tuple                |
# | ---------------- | ------------- | -------------------- |
# | Mutable          | Yes           | No                   |
# | Duplicates       | No            | Yes                  |
# | Indexing         | No            | Yes                  |
# | Ordered sequence | No            | Yes                  |
# | Main purpose     | Unique values | Fixed ordered values |
