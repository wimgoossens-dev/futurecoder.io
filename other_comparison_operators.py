# Example
sentence = "The e key on my keyboard is broken"
new_sentence = ""
for c in sentence:
    if c != "e":
        new_sentence += c
print(new_sentence)

# First exercise asks what the grade will be upfront, answer is <80 = "B"
percentage = 73

if percentage < 40:
    grade = "F"
elif percentage < 60:
    grade = "C"
elif percentage < 80:
    grade = "B"
else:
    grade = "A"
    
print(grade)

# My solution:
x1 = 30
x2 = 10
x3 = 20
lowestValue = ""

if x1 > x2:
    lowestValue = x2
else:
    lowestValue = x1
if lowestValue > x3:
    lowestValue = x3
print(lowestValue)

# Textbook solution 1:
if x1 < x2:
    if x1 < x3:
        first = x1
    else:
        first = x3
else:
    if x2 < x3:
        first = x2
    else:
        first = x3

print(first)

# Second solution provided by the textbook
first = x1

if x2 < first:
    first = x2

if x3 < first:
    first = x3

print(first)