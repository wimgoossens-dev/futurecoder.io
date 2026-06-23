# These technical details are often mistunderstood ("==" vs "is"): 
list1 = [1, 2, 3]
list2 = [1, 2, 3]

print(list1)
print(list2)
print(list1 == list2)

print(list1 is list2)

list1.append(4)

print(list1)
print(list2)
print("-------------")

# above is not the same as:
list1 = [1, 2, 3]
list2 = list1

print(list1)
print(list2)
print(list1 == list2)

print(list1 is list2)

list1.append(4)

print(list1)
print(list2)

# 