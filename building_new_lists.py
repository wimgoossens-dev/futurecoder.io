# First exercise
numbers = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1028]
doubled = []

for number in numbers:
    doubled += [number + number]
print(doubled)

# My solution to the second exercise
numbers = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1028]
greaterThanFiveList = []
for number in numbers:
    if number > 5:
        greaterThanFiveList.append(number)

print(greaterThanFiveList)
