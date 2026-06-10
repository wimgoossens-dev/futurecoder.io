# Exercise
things = ["This", "is", "a", "list"]
thing_to_find = "is"

found = False
for thing in things:
    if thing == thing_to_find:
        found = True

print(found)

things = ["This", "is", "a", "list"]
thing_to_find = "other"

found = False
for thing in things:
    if thing == thing_to_find:
        found = True

print(found)

# Optimized solution
things = ["This", "is", "a", "list"]
thing_to_find = "other"

for thing in things:
    if thing == thing_to_find:
        found = True
        break

print(found)
