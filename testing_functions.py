# assert_equal function to write tests
def assert_equal(actual, expected):
    if actual == expected:
        print("OK")
    else:
        print(f"Error! {repr(actual)} != {repr(expected)}")
# Test what happens when you don't type repr to figure out what it does
'''
print(f"{'abc'} != {repr('abc')}")
'''
# First excercise, look at the print messages
'''
def double(x):
    return x * 2

assert_equal(double(2), 4)
assert_equal(double(5), 10)
'''
def double(x):
    return x * 3

def quadruple(x):
    return double(double(x))

assert_equal(double(2), 4)
assert_equal(double(6), 13)
assert_equal(quadruple(5), 20)
assert_equal(quadruple(3), 11)

# Second excercise, test with english description when things get complicated
def surround(string, sides):
    return sides + string + sides

assert_equal(surround("more", "++"), "++more++")
assert_equal(surround("the same", "="), "=the same=")