import random


def game():
    global wincount, losecount
    draw = False
    win = False
    lose = False

    options = ["Rock", "Paper", "Scissors"]

    x = input("Would you like to choose Rock, Paper or Scissors? ")
    y = random.choice(options)

    if x == y:
        draw = True
    elif x == "Rock" and y == "Scissors":
        win = True
    elif x == "Paper" and y == "Rock":
        win = True
    elif x == "Scissors" and y == "Paper":
         win = True
    else:
          lose = True

    if draw == True:
        print("You have both chosen", x, "which has resulted in a draw")
    elif win == True:
        print("You have chosen", x, "and your opponent has chosen", y, "which has resulted in a win for you")
        wincount = wincount + 1
    elif lose == True:
        print("You have chosen", x, "and your opponent has chosen", y, "which has resulted in a loss for you")
        losecount = losecount + 1

wincount = 0
losecount = 0

best = input("Please enter the number for one of the following: \n 1. Best of 1 \n 2. Best of 3 \n 3. Best of 5 \n")
if int(best) == 1:
    game()
    print("Score: ", wincount, "-", losecount)
    if wincount == 1:
        print("Congrats!!!! You have won the match.")
    elif losecount == 1:
        print("Sorry! You have lost the match :(")
elif int(best) == 2:
    while wincount < 2 and losecount < 2:
        game()
        print("Score: ", wincount, "-", losecount)
    if wincount == 2:
        print("Congrats!!!! You have won the match.")
    elif losecount == 2:
        print("Sorry! You have lost the match :(")
elif int(best) == 3:
    while wincount < 3 and losecount < 3:
        game()
        print("Score: ", wincount, "-", losecount)
    if wincount == 3:
        print("Congrats!!!! You have won the match.")
    elif losecount == 3:
        print("Sorry! You have lost the match :(")
