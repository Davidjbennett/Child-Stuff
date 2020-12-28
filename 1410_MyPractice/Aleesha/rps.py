from random import *

def rockPaperScissors(user,npc):
    if user == 1 and npc == 1:
        print("Tie")
    elif user == 1 and npc == 2:
        print("NPC Wins")
    elif user == 1 and npc == 3:
        print("User Wins!")
    elif user == 2 and npc == 1:
        print("User Wins")
    elif user == 2 and npc == 2:
        print("Tie")
    elif user == 2 and npc == 3:
        print("NPC Wins")
    elif user == 3 and npc == 1:
        print("NPC Wins")
    elif user == 3 and npc == 2:
        print("User Wins")
    else:
        print("Tie")

userIn = ""
print("Welcome to RPS!")
userIn = input("Enter Rock, Paper, Scissors, or Quit: ")


if userIn.lower() == "rock":
    rInt = randint(1,3)
    print(rInt)
    rockPaperScissors(1, rInt)
elif userIn.lower() == "paper":
    rInt = randint(1,3)
    # RPS(2,rInt)
elif userIn.lower() == "scissors":
    rInt = randint(1,3)
    # RPS(3,rInt)
else:
    print("Invalid Entry!")


