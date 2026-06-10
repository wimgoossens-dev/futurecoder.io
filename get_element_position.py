# Example
words = ["This", "is", "a", "list"]

print(words[0])
print(words[1])
print(words[2])
print(words[3])
#print(words[4]) gives out of range error because the count starts with 0

# Exercise 1 with range
'''
words = ["This", "is", "a", "list"]
indices = [1, 2, 3, 4]

for index in indices:
    print(index)
    print(words[index])
'''

# Indices can be written easier, certainly for large lists
words = ["This", "is", "a", "list"]
indices = range(4)

for index in indices:
    print(index)
    print(words[index])
    
# Exercise 2
indices = range(4)

print(indices[0])
print(indices[1])
print(indices[2])
print(indices[3])

# Example 1 with the len function
words = ["This", "is", "a", "list"]
print(len(words))

# Example 2
words =["Hello", "world"]
word = ""
print(words[len(words)-1]) #print[(len(words))-1] was what I tried

#Example 3
words = ['This', 'is', 'a', 'list']

for index in range(len(words)):
    print(index)
    print(words[index])
