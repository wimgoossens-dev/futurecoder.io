# Print the first letter of the second string in the list.
strings = ["abc", "def", "ghi"]
print(strings[1][0])

# Print the last letter of the second-to-last string in the list "strings", you're not allowed to use "len" and your solution should work for any non-empty list of strings.
strings = ["abc", "def", "ghi"]
print(strings[-2][-1])

# What does the following program print?
strings = [["hello", "there"],["how", "are", "you"]]
print(strings[1][0])

# Now print the first letter of the third string in the second sublist.
strings = [["hello", "there"],["how", "are", "you"]]
print(strings[1][2][0])

# Append today to the second list.
strings = [["hello", "there"],["how", "are", "you"]]
strings[1].append("today?")
print(strings[1])

