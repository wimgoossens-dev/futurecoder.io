# Booleans
condition = True
print(condition)
condition = False
print(condition)

# Example
if True:
    print("This gets printed")
if False:
    print("This does not")

# Statement is true
sentence = "Hello World"
excited = True
if excited:
    sentence += "!"
print(sentence)

# Statement is false
sentence = "Hello World"
excited = False
if excited:
    sentence += "!"
print(sentence)

# Include an extra parameter "confused"
sentence = "Hello World"
excited = False
confused = True
if excited:
    sentence += "!"
if confused:
    sentence += "?"
print(sentence)