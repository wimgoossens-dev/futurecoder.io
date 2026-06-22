# A method is a function which belongs to a type that can be called on e.g. upper
word = "Hello"
print(word.upper)
print(word.upper())

# Another method is append
'''
word = "Hello"
word.append("!")
'''

# How does this work with lists?
nums = [1, 2, 3]
new_nums = nums + [4, 5]
print(new_nums)
print(nums)
nums.append(4)
print(nums)

# Exercise 1
nums = [1, 2, 3]
nums[1] = 9
print(nums)

# Exercise 2
[7, 8, 9, 8].index(8)

# Exercise 3 -> some_list.pop(index)
nums = [1, 2, 3]
print(nums.pop(1))
print(nums)

# Exercise 4 -> some_list.remove(value)
nums = [1, 2, 3]
nums.remove(1)
print(nums)

# Exercise 5. modify x to ["b", "c", "a"]
x = ['a', 'b', 'c']
x.append(x.pop(0))
print(x)

# Exercise 6. modify x to ["a", "b", "a"]
x = ['a', 'b', 'c']
x[len(x) - 1] = x[0]
print(x)

# Exercise 7. modify x with the first element repeated at the end and print as y
x = ['a', 'b', 'c']
y = x + [x[0]]
print(y)

# Exercise 8. replace line 2 with a line from the list that does the same thing
x = [1, 2, 0, 3]
x.pop(x.index(0))
print(x)