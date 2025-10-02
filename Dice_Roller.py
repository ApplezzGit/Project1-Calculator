from random import randrange

print("Dice Roller")
print("===========\n")

Entered = False
Increment = 1
while Entered == False:
    try:
        Dice = int(input("What type of dice would you like to roll?\n1) D4\n2) D6\n3) D8\n4) D10\n5) D12\n6) D20\n"))
        Entered = True
    except ValueError:
        print("Please enter a valid number.")
        Entered = False
Entered = False
while Entered == False:
    try:
        Number = int(input("How many dice would you like to roll?\n"))
        Entered = True
    except ValueError:
        print("Please enter a valid number.")
        Entered = False

while Increment <= Number:
    if Dice == 1:
        Roll = randrange(1, 5)
        print(f"Roll Result {Increment}: {Roll}")
    if Dice == 2:
        Roll = randrange(1, 7)
        print(f"Roll Result {Increment}: {Roll}")
    if Dice == 3:
        Roll = randrange(1, 9)
        print(f"Roll Result {Increment}: {Roll}")
    if Dice == 4:
        Roll = randrange(1, 11)
        print(f"Roll Result {Increment}: {Roll}")
    if Dice == 5:
        Roll = randrange(1, 13)
        print(f"Roll Result {Increment}: {Roll}")
    if Dice == 6:
        Roll = randrange(1, 21)
        print(f"Roll Result {Increment}: {Roll}")
    Increment += 1