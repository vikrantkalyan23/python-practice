# Logical operators combine multiple conditions

# and
# or
# not

# and requires both conditions to be true

# Condition A AND Condition B
# True  + True  → True
# True  + False → False
# False + True  → False
# False + False → False

age = 25
has_id = True
if age >= 18 and has_id:
    print("Allowed")

# or requires at least one condition to be true.

# Condition A OR Condition B
# True  OR True  → True
# True  OR False → True
# False OR True  → True
# False OR False → False

is_admin = False
is_manager = True
if is_admin or is_manager:
    print("Access granted")
    
# not reverses a Boolean value.

# not True  → False
# not False → True

is_logged_in = False
if not is_logged_in:
    print("Please login")
    
# Example  
is_logged_in = True
has_payment_method = True
if is_logged_in and has_payment_method:
    print("You can place the order")