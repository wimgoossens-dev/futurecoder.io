# Snoop is the debugger inside futurecoder.io
sentence = "Hello World"

include = False
new_sentence = ""
for char in sentence:
    if include:
        new_sentence += char
    include = True

print(new_sentence)

# This will output the exact opposite
sentence = "Hello World"

include = True
new_sentence = ""
for char in sentence:
    if include:
        new_sentence += char
    include = False

print(new_sentence)