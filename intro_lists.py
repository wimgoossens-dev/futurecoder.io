# Example 1
words = ["this", "is", "a", "list"]

for word in words:
    print(word)

# Example 2
x = 1
things = ["Hello", x, x + 3]
print(things)

numbers = [3, 1, 4, 1, 5, 9]

total = 0
for number in numbers:
    total += number

print(total)

# Exercise
words = ["This", "is", "a", "list"]
sentence = ""
separator = " - "

for word in words:
        sentence += word
        
print(sentence)

# My solution to the bonus exercise
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
