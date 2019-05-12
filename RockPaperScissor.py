import sys

User1 = input("What is your name: ")
User2 = input("What is your name: ")
Us1 = input("%s, do you select - rock, paper or scissor: " % User1)
Us2 = input("%s, do you select - rock, paper or scissor: " % User2)

def decide(u1,u2):
    if u1 == u2:
        return("It is a tie")
    elif u1 == "rock":
        if u2 == "paper": 
            return("paper wins")
        elif u2 == "scissors":
            return("rock wins")
    elif u1 == "paper":
        if u2 == "rock":
            return ("paper wins")
        elif u2 == "scissors":
            return("scissors wins")
    elif u1 == "scissors":
        if u2 == "rock":
            return("rock wins")
        elif u2 == "paper":
            return("scissors wins")
    else:
        print("You have made an invalid entry")
        sys.exit()

print(decide(Us1, Us2))

input("Press Enter to exit")