import random 

while True:
    user_action = input("enter a choice(rock,paper,scissors)")
    possible_actions = ["rock","paper","scissors"]

    computer_action =random.choice(possible_actions)
    print(f"\nYou choose  {user_action},compuet choose {computer_action}")

    if user_action == computer_action:
        print("lol it is a tie try again")
    elif user_action == "rock":
        if computer_action == "scissors":
            print("lets go you win")
        else:
            print("you lose lol")
    elif user_action == "paper":
            if computer_action == "rock":
                print("lets go you win")
            else:
                print("you lose lol")
    elif user_action == "scissors":
            if computer_action == "paper":
                print("lets go you win")
            else:
                print("you lose lol")
    