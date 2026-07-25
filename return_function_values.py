# Returning values instead of just printing them
def double(x):
    return x * 2

number = 5
twice = double(number)
print(number)
print(twice)

#Write a function "quadruple" which takes one argument 'x' and returns that argument x4 but you can only use the "double" function
def double(x):
    return x * 2

def quadruple(x):
    return double(double(x))

number = 5
print(quadruple)
