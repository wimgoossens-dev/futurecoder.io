name = "World"
line = ""

for char in name:
    line = line + char
    print(line)

name = "World"
line = ""

for char in name:
    line = char + line
    print(line)

name = input('Please enter your name so I can decorate it properly: ')
line = ''

for char in name:
    line += '-'
        
print('+' + line + '+')
print('|' + name + '|')    
print('+' + line + '+')