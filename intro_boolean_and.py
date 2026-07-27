# Rewrite the function below without or
'''
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
'''

def is_valid_percentage(x):
    if x >= 0 and x <= 100: #return 0 <= x and x <= 100 replaces these 4 lines
        return True
    else:
        return False

assert_equal(is_valid_percentage(-1), False)
assert_equal(is_valid_percentage(0), True)
assert_equal(is_valid_percentage(50), True)
assert_equal(is_valid_percentage(100), True)
assert_equal(is_valid_percentage(101), False)

# Check if all elements are equal
def all_equal(row):
    return row[0] == row[1] and row[0] == row[2] #return row[0] == row[1] == row[2] for shorter notation

assert_equal(all_equal(["X", "X", "X"]), True)
assert_equal(all_equal(["O", "O", "O"]), True)
assert_equal(all_equal(["X", "O", "X"]), False)

