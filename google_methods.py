# Don't learn all the functions but look them up, here are some examples:
'''
*append
python add element to list
python add item at end of list

*len
python size of list
python number of elements in list
python how many characters in string

*sum
python add list of numbers
python total of numbers

*in
python check if list contains value
python test if list has element

*index
python get position of element
python get index of value
'''

# Exercise 1
print(max([21, 55, 4, 91, 62, 49]))

# Exercise 2 with solution from the book which assumes you know the position
nums = [1, 2, 3, 4, 5]
nums.insert(2, 9)
print(nums)

# Exercise 2 with my solution that calculates the position with // for rounding since a position has to be a whole number 
nums = [1, 2, 3, 4 , 5]
mid = len(nums) // 2
nums.insert(mid, 9)
print(nums)

# dir([]) and dir() in the shell gives you a list of the argument's attributes which are mostly methods