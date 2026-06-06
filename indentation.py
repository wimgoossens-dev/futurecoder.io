name = "World"

for char in name:
    print(char)
    print("---")

'''
Since print("---") is not indented, it's not part of the loop body.
This means it only runs once, after the whole look has finished running.
They are both valid doing different things.
'''
for char in name:
    print(char)
print("---")