# Implement "print_twice" using "print_many"
def print_many(n,thing):
    for _ in range(n):
        print(thing)

def print_twice(x):
    print_many(2,x)

print_twice("Hello")