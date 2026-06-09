# Example
dna = 'AGTAGCGTC'
opposite_dna = ''
for char in dna:
    if char == 'A':
        char = 'T'
    if char == 'T':
        char = 'A'
    if char == 'G':
        char = 'C'
    if char == 'C':
        char = 'G'
    opposite_dna += char

print(opposite_dna)

# Exercise
dna = "AGTAGCGTC"
opposite_dna = ""
for char in dna:
    if char == "A":
        char = "T"
    else:
        if char == "T":
            char = "A"
    if char == "G":
        char = "C"
    else:
        if char == "C":
            char = "G"
    
    opposite_dna += char

print(opposite_dna)

# More efficient program with elif
dna = "AGTAGCGTC"
opposite_dna = ""

for char in dna:
    if char == "A":
        char = "T"
    elif char == "T":
        char = "A"
    elif char == "G":
        char = "C"
    elif char == "C":
        char = "G"
    opposite_dna += char
    
print(opposite_dna)

#
