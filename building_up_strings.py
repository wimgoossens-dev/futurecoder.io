# Modify this program
name = "World"
line = ""

for char in name:
    line = line + char
    print(line)

# Program it backwards
name = "World"
line = ""

for char in name:
    line = char + line
    print(line)

# Extend your program to draw a box around the name
name = input("Please enter your name so I can decorate it properly: ")
line = ""

for char in name:
    line += "-"
        
print("+" + line + "+")
print("|" + name + "|")    
print("+" + line + "+")

# Now the name should be the box
line = ""

for char in name:
    line += " "
        
print("+" + name + "+")

for char in name:
    print(char + line + char)
    
print("+" + name + "+")

# Write the name diagonal
line = ""

for char in name:
    print(line + char)
    line += " "
