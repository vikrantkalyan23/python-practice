# Identity operators check whether two variables refer to the same object

# is
# is not

# is
a = None
print(a is None)

if a is None:
    print("No result")

# is not
result = "Success"
if result is not None:
    print(result)
    
# == vs is
# This is an important Python concept.
# == asks:
# Do these objects have equal values?
# is asks:
# Are these the same object?

# For example:
a = [1, 2, 3]
b = [1, 2, 3]
print(a == b)
print(a is b)

