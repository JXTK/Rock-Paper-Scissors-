""" Rock Paper Scissors
----------------------------------------
"""
import random
import sys
import time

t = 10
counter = 0
userWins = 0
compWins = 0
tie = 0


def countdown(t):
    while t:
        mins, secs = divmod(t, 60)
        timer = '{:02d}'.format(secs)
        print(timer, end="\r")
        time.sleep(1)
        t -= 1
    print('Exiting Now!')


def play():
    counter=0
    userWins=0
    compWins=0
    tie=0
    while counter <= rounds - 1:
        opponentChoice = input(
            "Enter your weapon, [R]ock, [P]aper, [S]cissors: ")
        computerChoice = random.randint(1, 3)  
				#1 means Rock
        #2 means Paper
        #3 means Scissors

        #computerChoice=="Rock"
        if opponentChoice == "R" and computerChoice == int(1):
            print(" You chose: Rock")
            print(" I chose : Rock")
            print(" It's a tie")
            counter += 1
            tie += 1
        elif opponentChoice == "r" and computerChoice == int(1):
            print(" You chose: Rock")
            print(" I chose : Rock")
            print(" It's a tie")
            counter += 1
            tie += 1
        elif opponentChoice == "P" and computerChoice == int(1):
            print("You chose: Paper")
            print("I choose: Rock")
            print("Paper cover rock, you win!")
            counter += 1
            userWins += 1
        elif opponentChoice == "p" and computerChoice == int(1):
            print("You chose: Paper")
            print("I choose: Rock")
            print("Paper cover rock, you win!")
            counter += 1
            userWins += 1
        elif opponentChoice == "S" and computerChoice == int(1):
            print("You chose: Scissors")
            print("I choose: Rock")
            print("Rock smash Scissor, I win!")
            counter += 1
            compWins += 1
        elif opponentChoice == "s" and computerChoice == int(1):
            print("You chose: Scissors")
            print("I choose: Rock")
            print("Rock smash Scissor, I win!")
            counter += 1
            compWins += 1

        #computerChoice=="Paper"
        if opponentChoice == "R" and computerChoice == int(2):
            print(" You chose: Rock")
            print(" I chose : Paper")
            print("Paper cover rock, I win!")
            counter += 1
            compWins += 1
        elif opponentChoice == "r" and computerChoice == int(2):
            print(" You chose: Rock")
            print(" I chose : Paper ")
            print("Paper cover rock, I win!")
            counter += 1
            compWins += 1
        elif opponentChoice == "P" and computerChoice == int(2):
            print("You chose: Paper")
            print("I choose: Paper")
            print("It's a tie.")
            counter += 1
            tie += 1
        elif opponentChoice == "p" and computerChoice == int(2):
            print("You chose: Paper")
            print("I choose: Paper")
            print("It's a tie")
            counter += 1
            tie += 1
        elif opponentChoice == "S" and computerChoice == int(2):
            print("You chose: Scissors")
            print("I choose: Paper")
            print("Scissor cut paper, you win!")
            counter += 1
            userWins += 1
        elif opponentChoice == "s" and computerChoice == int(2):
            print("You chose: Scissors")
            print("I choose: Paper")
            print("Scissor cut Paper, you win!")
            counter += 1
            userWins += 1

        #computerChoice=="Scissors"
        if opponentChoice == "R" and computerChoice == int(3):
            print(" You chose: Rock")
            print(" I chose : Scissors")
            print("Rock smash Scissor, you win!")
            counter += 1
            userWins += 1
        elif opponentChoice == "r" and computerChoice == int(3):
            print(" You chose: Rock")
            print(" I chose : Scissors")
            print("Rock smash Scissor, you win!")
            counter += 1
            userWins += 1
        elif opponentChoice == "P" and computerChoice == int(3):
            print("You chose: Paper")
            print("I choose: Scissors")
            print("Scissor cut Paper, I win!")
            counter += 1
            compWins += 1
        elif opponentChoice == "p" and computerChoice == int(3):
            print("You chose: Paper")
            print("I choose: Scissors")
            print("Scissor cut Paper, I win!")
            counter += 1
            compWins += 1
        elif opponentChoice == "S" and computerChoice == int(3):
            print("You chose: Scissors")
            print("I choose: Scissors")
            print("It's a tie.")
            counter += 1
            tie += 1
        elif opponentChoice == "s" and computerChoice == int(3):
            print("You chose: Scissors")
            print("I choose: Scissors")
            print("It's a tie.")
            counter += 1
            tie += 1
  
    else:
        print(
            "\n___________________________RESULTS_____________________________"
        )
        print("You won: ", userWins)
        print("I won: ", compWins)
        print("Ties (if any):", tie)
        if userWins == compWins:
            print("Game tied between user and computer.")
        elif userWins > compWins:
            print("You won this gsme. Well played.")
        elif userWins < compWins:
            print("I won this game, but well played from your side too.")
        print(
            "_________________________________________________________________"
        )

    playAgain = input(
        "So, do you want to play again, or are you too chicken? [y/n] ")
    if playAgain == "y":
			  play()
    elif playAgain == "n":
        countdown(t)
    else:
        sys.exit()


print("---------------------------------------------------------------")
print()
print(
    "Welcome to this game of ROCK, PAPER, SCISSORS. \n If you didn't know, Rock paper scissors is a hand game usually played between two people, in which each player simultaneously forms one of three shapes with an outstretched hand. "
)
print()
print("Do you want to play with an expert like me, or are you a scaredy cat? ")
y_n = input("Type 'y' if yes and 'n' if no. ")
print()
if y_n == "y":
    rounds = int(
        input(
            "How many rounds do you want to play with me? Minimum 1. "
        ))

    while counter <= rounds - 1:
        opponentChoice = input(
            "Enter your weapon, [R]ock, [P]aper, [S]cissors: ")
        computerChoice = random.randint(1, 3)  #1 means Rock
        #2 means Paper
        #3 means Scissors

        #computerChoice=="Rock"
        if opponentChoice == "R" and computerChoice == int(1):
            print(" You chose: Rock")
            print(" I chose : Rock")
            print(" It's a tie")
            counter += 1
            tie += 1
        elif opponentChoice == "r" and computerChoice == int(1):
            print(" You chose: Rock")
            print(" I chose : Rock")
            print(" It's a tie")
            counter += 1
            tie += 1
        elif opponentChoice == "P" and computerChoice == int(1):
            print("You chose: Paper")
            print("I choose: Rock")
            print("Paper cover rock, you win!")
            counter += 1
            userWins += 1
        elif opponentChoice == "p" and computerChoice == int(1):
            print("You chose: Paper")
            print("I choose: Rock")
            print("Paper cover rock, you win!")
            counter += 1
            userWins += 1
        elif opponentChoice == "S" and computerChoice == int(1):
            print("You chose: Scissors")
            print("I choose: Rock")
            print("Rock smash Scissor, I win!")
            counter += 1
            compWins += 1
        elif opponentChoice == "s" and computerChoice == int(1):
            print("You chose: Scissors")
            print("I choose: Rock")
            print("Rock smash Scissor, I win!")
            counter += 1
            compWins += 1

        #computerChoice=="Paper"
        if opponentChoice == "R" and computerChoice == int(2):
            print(" You chose: Rock")
            print(" I chose : Paper")
            print("Paper cover rock, I win!")
            counter += 1
            compWins += 1
        elif opponentChoice == "r" and computerChoice == int(2):
            print(" You chose: Rock")
            print(" I chose : Paper ")
            print("Paper cover rock, I win!")
            counter += 1
            compWins += 1
        elif opponentChoice == "P" and computerChoice == int(2):
            print("You chose: Paper")
            print("I choose: Paper")
            print("It's a tie.")
            counter += 1
            tie += 1
        elif opponentChoice == "p" and computerChoice == int(2):
            print("You chose: Paper")
            print("I choose: Paper")
            print("It's a tie")
            counter += 1
            tie += 1
        elif opponentChoice == "S" and computerChoice == int(2):
            print("You chose: Scissors")
            print("I choose: Paper")
            print("Scissor cut paper, you win!")
            counter += 1
            userWins += 1
        elif opponentChoice == "s" and computerChoice == int(2):
            print("You chose: Scissors")
            print("I choose: Paper")
            print("Scissor cut Paper, you win!")
            counter += 1
            userWins += 1

        #computerChoice=="Scissors"
        if opponentChoice == "R" and computerChoice == int(3):
            print(" You chose: Rock")
            print(" I chose : Scissors")
            print("Rock smash Scissor, you win!")
            counter += 1
            userWins += 1
        elif opponentChoice == "r" and computerChoice == int(3):
            print(" You chose: Rock")
            print(" I chose : Scissors")
            print("Rock smash Scissor, you win!")
            counter += 1
            userWins += 1
        elif opponentChoice == "P" and computerChoice == int(3):
            print("You chose: Paper")
            print("I choose: Scissors")
            print("Scissor cut Paper, I win!")
            counter += 1
            compWins += 1
        elif opponentChoice == "p" and computerChoice == int(3):
            print("You chose: Paper")
            print("I choose: Scissors")
            print("Scissor cut Paper, I win!")
            counter += 1
            compWins += 1
        elif opponentChoice == "S" and computerChoice == int(3):
            print("You chose: Scissors")
            print("I choose: Scissors")
            print("It's a tie.")
            counter += 1
            tie += 1
        elif opponentChoice == "s" and computerChoice == int(3):
            print("You chose: Scissors")
            print("I choose: Scissors")
            print("It's a tie.")
            counter += 1
            tie += 1

    else:
        print(
            "\n___________________________RESULTS_____________________________"
        )
        print("You won: ", userWins)
        print("I won: ", compWins)
        print("Ties (if any):", tie)
        if userWins == compWins:
            print("Game tied between user and computer.")
        elif userWins > compWins:
            print("You won this game. Well played.")
        elif userWins < compWins:
            print("I won this game, but well played from your side too.")
        print(
            "_________________________________________________________________"
        )

    playAgain = input(
        "So, do you want to play again, or are you too chicken? [y/n] ")
    if playAgain == "y":
			  play()
    elif playAgain == "n":
        countdown(t)
    else:
        sys.exit()

elif y_n == "n":
    print("Ok. Bye.")
    countdown(t)

else:
    sys.exit()

print("---------------------------------------------------------------")
