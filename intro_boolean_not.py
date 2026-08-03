# This test-function is needed for making the code work
def assert_equal(actual, expected):
    if actual == expected:
        print("OK")
    else:
        print(f"Error! {actual!r} != {expected!r}")

def invalid_image(filename):
    return not filename.endswith((".png", ".jpg"))

assert_equal(invalid_image("dog.png"), False)
assert_equal(invalid_image("cat.jpg"), False)
assert_equal(invalid_image("invoice.pdf"), True)