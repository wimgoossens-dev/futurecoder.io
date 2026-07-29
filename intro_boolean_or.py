# This test-function is needed for making the code work
def assert_equal(actual, expected):
    if actual == expected:
        print("OK")
    else:
        print(f"Error! {repr(actual)} != {repr(expected)}")

# The function below accepts one parameter, name, and checks if the person with the given name is among your friends
def is_friend(name):
    if name == "Alice":
        return True
    elif name == "Bob":
        return True
    else:
        return False

assert_equal(is_friend("Alice"), True)
assert_equal(is_friend("Bob"), True)
assert_equal(is_friend("Charlie"), False)

# Short notation for return with boolean
'''
def is_friend(name):
        if name == "Alice":
          return True
        elif name == "Bob":
          return True

assert_equal(is_friend("Alice"), True)
assert_equal(is_friend("Bob"), True)
assert_equal(is_friend("Charlie"), False)
'''
def is_friend(name):
        return name == "Alice" or name == "Bob" # common mistake here is to write return name == "Alice" or "Bob"

assert_equal(is_friend("Alice"), True)
assert_equal(is_friend("Bob"), True)
assert_equal(is_friend("Charlie"), False)

# Write a function named is_valid_percentage, one argument x, return True if 0 > x < 100 and return False otherwise
def is_valid_percentage(x):
    if x < 0 or x > 100:
        return False
    else:
        return True

assert_equal(is_valid_percentage(-1), False)
assert_equal(is_valid_percentage(0), True)
assert_equal(is_valid_percentage(50), True)
assert_equal(is_valid_percentage(100), True)
assert_equal(is_valid_percentage(101), False)
