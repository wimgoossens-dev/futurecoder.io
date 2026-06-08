# This is the more efficient solution as it only iterartes over the string if it needs to
sentence = "Hello World"
excited = True

if excited:
    new_sentence = ""
    for char in sentence:
        new_sentence += char + "!"
    sentence = new_sentence

print(sentence)

# This program has the exact same result but when excited = False nothing changes
sentence = "Hello World"
excited = True

new_sentence = ""
for char in sentence:
    new_sentence += char
    if excited:
        new_sentence += "!"
    
sentence = new_sentence
print(sentence)