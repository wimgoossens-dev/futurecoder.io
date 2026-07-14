# Predict the output of this code 
numbers = [[1, 2, 3], [4, 5], [6], []]

for sublist in numbers:
    for num in sublist:
        print(num)
    print("---")

# Search for a particular word deep within the list and print every string that contains that word
strings = [
    [
        "hello there",
        "how are you",
    ],
    [
        "goodbye world",
        "hello world",
    ]
]
word = "hello"

for sublist in strings:
    for item in sublist:
        if word in item:
            print(item)

# Print a boolean for each sublist
strings = [
    [
        "hello there",
        "how are you",
    ],
    [
        "goodbye world",
        "hello world",
    ]
]
word = "goodbye"

for sublist in strings:
    present = False
    for string in sublist:
        if word in string:
            present = True
    print(present)

# Print one boolean if word is present in any string in the entire nested list
strings = [
    [
        "hello there",
        "how are you",
    ],
    [
        "goodbye world",
        "hello world"
    ]
]
word = "Python"

present = False
for sublist in strings:
    for string in sublist:
        if word in string:
            present = True
print(present)

# Print the first letter of each string on one line do the same for second and third letter
strings = ["abc", "def", "ghi"]

first_letter = ""
second_letter = ""
third_letter = ""

for character in strings:
    first_letter = first_letter + character[0]
    second_letter = second_letter + character[1]
    third_letter = third_letter + character[2]
    
print(first_letter)
print(second_letter)
print(third_letter)

# Discover the hidden message from Zen Python!
strings = ["  b n", "f ete", "liths", "astat", "t ene", "  r d"]

for i in range(len(strings[0])):
    line = ""
    for string in strings:
        line += string[i]
    print(line)

# Bonus question <3
strings = ["abcqwe", "def", "ghiq"]

max_len = max(len(string) for string in strings)

for char in range(max_len):
    line = ""
    for string in strings:
        if char < len(string):
            line += string[char]
        else:
            line += " "
    print(line)