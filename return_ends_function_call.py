def assert_equal(actual, expected):
    if actual == expected:
        print("OK")
    else:
        print(f"Error! {repr(actual)} != {repr(expected)}")

# Guess what the output will be
def foo():
    return 1
    return 2

print(foo())

# If you want to return several values, return a list
def double_numbers(numbers):
    doubles = []
    for x in numbers:
        doubles.append(x * 2)
    return doubles

assert_equal(double_numbers([1, 2, 3]), [2, 4, 6])

# What happens with nested loops? (return stops the loop)
def foo():
    for letter in 'abc':
        for number in range(3):
            print(f"{letter} {number}")
            if letter == 'b':
                return letter

foo()

# Change return x with break
def foo():
    for letter in 'abc':
        for number in range(3):
            print(f"{letter} {number}")
            if letter == 'b':
                break

foo()