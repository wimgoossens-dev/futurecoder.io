words = ["this", "is", "a", "list"]

for word in words:
    print(word)

x = 1
things = ["Hello", x, x + 3]
print(things)

numbers = [3, 1, 4, 1, 5, 9]

total = 0
for number in numbers:
    total += number

print(total)

words = ["This", "is", "a", "list"]
sentence = ""
separator = " - "
firstWord = True

for word in words:
    if firstWord:
        sentence += word
        firstWord = False
    else:
        sentence += (separator + word)
    
print(sentence)
