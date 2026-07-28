# You need to tell Python that the first line is continuing onto the second line. Here are some examples, pay close attention to the details.
name = "Bob"

is_friend = name == "Alice" or \
            name == "Bob"
print(is_friend)

is_friend = (name == "Alice" or
             name == "Bob")
print(is_friend)

is_friend = [name == "Alice",
             name == "Bob"]
print(is_friend)

print(name == "Alice" or
      name == "Bob")
