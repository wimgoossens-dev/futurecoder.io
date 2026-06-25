# A nested loop is a loop inside a loop which can be useful to write interesting programs.
for letter in "ABC":
    print(letter)
    for number in range(4):
        print(f"{letter} {number}")
    print("---")

# Write a program for a multiplication table to twelve
for left in range(12):
    left += 1
    for right in range(12):
        right += 1
        product = left * right
        print(f"{left} x {right} = {product}")
    print("---")

# Some fun with the former multiplication table B-)
values = []
for left in range(1, 101):
    for right in range(1, 101):
        product = left * right
        print(f"{left} x {right} = {product}")
        values.append(product)
    print("---")
print(values)
number_count = int(input("What number would you like to count in the multiplication table?: "))
if values.count(number_count) > 0:
    print(f"The number you want to count appears {values.count(number_count)} times!")
else:
    print("The number you want to count doesn't appear in the list of products!")

# Write a matchmaker program with Alice, Bob and Charlie but they don't play themselves.
players = ["Alice", "Bob", "Charlie"]

for player1 in players:
    for player2 in players:
        if player1 != player2:
            print(f"{player1} vs {player2}")

# Write a program that cracks a 4 letter password "ABCD"
letters = "ABCD"

for letter1 in letters:
    for letter2 in letters:
        for letter3 in letters:
            for letter4 in letters:
                print(letter1+letter2+letter3+letter4)

# Print out an upside down triangle made of the '+' sign
size = int(input("What is the size at the top of your triangle?: "))
print()

for number in range(size):
    length = size - number
    line = ""
    for number in range(length):
        line += "+"
    print(line)

# A bonus exercise on the players exercise, now the pair only can show up one time.
players = ["Alice", "Bob", "Charlie", "Dylan"]

for player1 in range(len(players)):
    for player2 in range(len(players)):
        if player1 < player2:
            print(f"{players[player1]} vs {players[player2]}")