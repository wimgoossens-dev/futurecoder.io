# Never modify something while you iterate over it
'''
numbers = [10, 7, 8, 3, 12, 15]
for i in range(len(numbers)):
    number = numbers[i]
    if number <= 10:
        numbers.pop(i)
print(numbers)
'''

# This doesn't remove 7 or 3 in this example
numbers = [10, 7, 8, 3, 12, 15]
for number in numbers:
    if number <= 10:
        numbers.remove(number)
print(numbers)

# Iterate and modify a copy like in this example:
numbers = [10, 7, 8, 3, 12, 15]
for number in numbers.copy():
    if number <= 10:
        numbers.remove(number)
print(numbers)

# Similarly you could loop over the original and modify a copy:
numbers = [10, 7, 8, 3, 12, 15]
big_numbers = numbers.copy()

for number in numbers:
    if number <= 10:
        big_numbers.remove(number)
print(big_numbers)

# Build a new list from scratch
numbers = [10, 7, 8, 3, 12, 15]
big_numbers = []

for number in numbers:
    if number > 10:
        big_numbers.append(number)
print(big_numbers)

# To recap: Modify a copy / Iterate over a copy / Make a new version