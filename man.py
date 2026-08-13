import random
playing = True
number = str(random.randint(0,20))

print("I will randomly generate a number from 1 to 20 and you have to guess it correctly Good luck!")

while playing:
    guess = input("give me your best guess!")
    if number == guess:
        print("you win the game hurray!!!!!")
        print("the numebr was",number)
        break

    else:
        print("you lost try again")