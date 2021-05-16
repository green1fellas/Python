# Jenga

import random

turn = "1"

print("Welcome to Text-Based Jenga!")

while(True):
    pull = input("\nIt is now Player " + turn + "'s turn. Pull jenga piece?\n")
    if(pull.lower() == "yes" or pull.lower() == "pull"):
        success = random.randint(0,100)
        if(success > 5):
            print("Safe! You successfully pulled out the piece.")
        else:
            print("Oh no! The tower fell. Player " + turn + " loses.")
            break
    elif(pull.lower() == "no"):
        print("Okay, I guess we're not playing then.")
        break
    else:
        print("Invalid input. Please try again.")
        continue
    if(turn == "1"):
        turn = "2"
    else:
        turn = "1"
