# If Else statement
condition = False
if condition:
    print("Yes")
else:
    print("No")

# If excited print uppercase, otherwise just print lowercase
sentence = "Hello World"
excited = False
if excited:
    sentence = sentence.upper()
else:
    sentence = sentence.lower()
    
print(sentence)


# If excited print ! at the end of the sentence otherwise a .
sentence = "Hello World"
excited = False

if excited:
    char = "!"
    sentence += char
else:
    char = "."
    sentence += char

print(sentence)


# An exercise to see if you can print first letter with a capital letter no matter the input
sentence = "hello there"
new_sentence = ""
firstLetter = True
user_excited = input("Are you excited? (y or n)").strip().lower()
if user_excited == "y":
    excited = True
else:
    excited = False


for char in sentence:
    if firstLetter:
        char = char.upper()
    else:
        char = char.lower()
    new_sentence += char
    firstLetter = False
    
    
if excited:
    sign = "!"
    sentence += char
else:
    sign = "."
    sentence += char
    
print(new_sentence + sign)


# Alternate uppercase with lowercase
sentence = "hello there"
new_sentence = ""
upper = True

for char in sentence:
    if upper:
        char = (char).upper()
        new_sentence += char
        upper = False
    else:
        char = (char).lower()
        new_sentence += char
        upper = True
    
print(new_sentence)


# Test for a longer sentence
sentence = "one more exercise, and then you can relax."
new_sentence = ""
upper = True

for char in sentence:
    if upper:
        char = (char).upper()
        new_sentence += char
        upper = False
    else:
        char = (char).lower()
        new_sentence += char
        upper = True
    
print(new_sentence)
