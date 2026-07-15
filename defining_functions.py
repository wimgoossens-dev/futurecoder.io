# Define a function called "greet" which accepts one parameter
def greet(name):
    print(f"Hello {name}!")

greet("Alice")
greet("Bob")
print()

# Predict the outcome
def greet(name):
    print(f"Hello {name}!")
    print("How are you?")
    
greet("Alice")
greet("Bob")
print()
# Change the name of the function form greet to say_hello and name to person_name
def say_hello(person_name):
    print(f"Hello {person_name}!")
    print("How are you?")
    
say_hello("Alice")
say_hello("Bob")
print()

# Write a function called "print_twice" with one argument "x" that prints the argument twice
def print_twice(x): 
    print(x)
    print(x)

print_twice("Hello")
print()

# Functions can have many parameters
def print_many(thing, n):
        for _ in range(n):
            print(thing)

print_many("Hello", 3)
print()

# It is possible to swap around the parameters from the previous example but make sure to adjust them in the print statement like shown in this example underneath
def print_many(thing, n):
    for _ in range(n):
        print(thing)

print_many(3, "Hello")