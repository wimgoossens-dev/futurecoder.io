# Methods for strings
print("the" in "feed the dog and cat")

string = "feed the dog ant the cat"
print(string.count("the"))
print(string.index("the"))

# Strings unlike lists are immutable -> "str" object has no attribute "append"
'''
"Python".append("is cool!")
'''

# The referred string isn't modified you have to assign a new value to the variable:
sentence = "Python rocks!"
new_sentence = sentence.upper()
print(sentence)
print(new_sentence)