# Example
print(1 + 2 == 3)
print(4 + 5 == 6)
print('ab' + 'c' == 'a' + 'bc')

# Exercise
name = "kesha"
new_name = ""
for c in name:
    if c == "s":
        c = "$"
    if c == "e":
        c = "3"
    if c == "a":
        c = "@"
    new_name += c

print(new_name)